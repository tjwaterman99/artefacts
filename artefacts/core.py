"""
The core module contains the deserialized dbt artifacts, and various objects such
as models, tests, and sources.

>>> from artefacts import Manifest, RunResults, Sources, Catalog

To use an artefact, you first need to `load` it.

>>> manifest = Manifest.load()
"""

import datetime
import uuid
import os
import json
import re
import pydantic
import typing
import packaging.version

import artefacts.state
from artefacts.config import conf


Catalog = typing.ForwardRef('Catalog')
CatalogNode = typing.ForwardRef('CatalogNode')
CatalogNodeColumn = typing.ForwardRef('CatalogNodeColumn')
CatalogNodeMetadata = typing.ForwardRef('CatalogNodeMetadata')
CatalogNodeStats = typing.ForwardRef('CatalogNodeStats')
Manifest = typing.ForwardRef('Manifest')
ManifestDocsNode = typing.ForwardRef('ManifestDocsNode')
ManifestExposureNode = typing.ForwardRef('ManifestExposureNode')
ManifestMacroNode = typing.ForwardRef('ManifestMacroNode')
ManifestMetricNode = typing.ForwardRef('ManifestMetricNode')
ManifestNode = typing.ForwardRef('ManifestNode')
ManifestNodeReference = typing.ForwardRef('ManifestNodeReference')
ManifestSourceNode = typing.ForwardRef('ManifestSourceNode')
Metadata = typing.ForwardRef('Metadata')
ResultTiming = typing.ForwardRef('ResultTiming')
RunResultNode = typing.ForwardRef('RunResultNode')
RunResults = typing.ForwardRef('RunResults')
Sources = typing.ForwardRef('Sources')
SourcesFreshnessResult = typing.ForwardRef('SourcesFreshnessResult')


class Artifact:

    @classmethod
    def path(cls):
        """The path to the artifact.
        
        The path is determined by the :ref:`configuration` settings. By default
        artefacts will look in the `./target` directory of the current working 
        directory.
        """
        
        return os.path.join(conf.dbt_target_dir, cls.name() + '.json')

    @classmethod
    def name(cls):
        """The name of the artifact in snake_case.
        """

        return re.sub(r'(?<!^)(?=[A-Z])', '_', cls.__name__).lower()

    @classmethod
    def load(cls):
        """Load and deserialize the artifact.
        
        The deserialized artifact is cached, so calling this function twice will
        not update the artifact if it has been rebuilt.

        In general, loading the artifacts is not necessary, and most tasks can
        be accomplished by using the :ref:`api` module instead of working with
        the artifact classes directly. 
        """

        if not artefacts.state.exists(cls.name()):
            with open(cls.path(), 'r') as artifact_fh:
                raw_artifact = json.load(artifact_fh)
            artefacts.state.set(cls.name(), cls.parse_obj(raw_artifact))              
        return artefacts.state.get(cls.name())  


class ArtifactReader:

    @property
    def run_results_artifact(self) -> RunResults:
        """A reference to the :class:`RunResults` artifact. """

        return self.get_artifact('run_results')

    @property
    def manifest_artifact(self) -> Manifest:
        """A reference to the :class:`Manifest` artifact. """
        
        return self.get_artifact('manifest')

    @property
    def catalog_artifact(self) -> Catalog:
        """A reference to the :class:`Catalog` artifact. """

        return self.get_artifact('catalog')

    @property
    def sources_artifact(self) -> Sources:
        """A reference to the :class:`Sources` artifact. """

        return self.get_artifact('sources')
    
    def get_artifact(self, artifact_name):
        if artefacts.state.exists(artifact_name):
            return artefacts.state.get(artifact_name)
        else:
            artifact = {
                'manifest': Manifest,
                'run_results': RunResults,
                'sources': Sources,
                'catalog': Catalog
            }.get(artifact_name)

            if artifact is None:
                raise AttributeError(f"Invalid artifact name: {artifact_name}")
            
            return artifact.load()


class ArtifactNodeReader(ArtifactReader):
    
    @property
    def manifest(self):
        """A reference to details about the node contained in the manifest."""

        # TODO: what if the resource_type is `source`? I don't think it will
        # show up in the `nodes` reference.
        return self.manifest_artifact.nodes.get(self.unique_id)

    @property
    def catalog(self):
        """A reference to details about the node contained in the catalog."""

        return self.catalog_artifact.nodes.get(self.unique_id)

    @property
    def run_results(self):
        """A reference to results from running the node, if it exists."""

        return [r for r in self.run_results_artifact.results if r.unique_id == self.unique_id]

    @property
    def parents(self):
        """ A list of the node's parents """

        return self.manifest_artifact.parent_map[self.unique_id]

    @property
    def children(self):
        """ A list of the node's children """

        return self.manifest_artifact.child_map[self.unique_id]

    @property
    def tests(self):
        """ A list of any tests that reference the node """

        return [t for t in self.children if t.resource_type == 'test']

    @property
    def snapshots(self):
        """ A list of any snapshots that reference the node """

        return [s for s in self.children if s.resource_type == 'snapshot']


class Manifest(Artifact, pydantic.BaseModel):
    """
    The manifest artifact.

    Attributes:
        metadata: reference to the Manifest's metadata
        nodes: reference to the Manifest's nodes
        sources: reference to the Manifest's sources
        macros: reference to the Manifest's macros
        docs: reference to the Manifest's docs
        exposures: reference to the Manifest's exposures
        metrics: reference to the Manifest's metrics
        selectors: reference to the Manifest's selectors
        disabled: reference to the Manifest's disabled
        parent_map: reference to the Manifest's parent_map
        child_map: reference to the Manifest's child_map

    """

    metadata: Metadata
    nodes: typing.Dict[str, ManifestNode]
    sources: typing.Dict[str, ManifestSourceNode]
    macros: typing.Dict[str, ManifestMacroNode]
    docs: typing.Dict[str, ManifestDocsNode]
    exposures: typing.Dict[str, ManifestExposureNode]
    metrics: typing.Dict[str, ManifestMetricNode]
    selectors: dict
    disabled: typing.Union[dict, None]
    parent_map: typing.Union[typing.Dict[str, typing.List[ManifestNodeReference]], None]
    child_map: typing.Union[typing.Dict[str, typing.List[ManifestNodeReference]], None]

    class Config:
        arbitrary_types_allowed = True


class RunResults(Artifact, pydantic.BaseModel):
    """The run_results artifact. 
    
    Attributes:
        metadata: The :class:`Metadata` associated with the run, such as when
                  the run was generated, the environment variables present
                  during the run, etc.
        results: A list of :class:`RunResultNode` s, which contain details 
                 about how long each node ran, whether it was successful, etc.
        elapsed_time: The total duration of the run
        args: The arguments used when at the start of the run or build
    
    """

    metadata: Metadata
    results: typing.List[RunResultNode]
    elapsed_time: float
    args: typing.Union[dict, None]


class Catalog(Artifact, pydantic.BaseModel):
    """The catalog artifact. 
    
    Attributes:
        metadata: The metadata attribute of the catalog
        nodes: The nodes attribute of the catalog
        sources: The sources attribute of the catalog
        errors: The errors attribute of the catalog
    
    """

    metadata: Metadata
    nodes: typing.Dict[str, CatalogNode]
    sources: typing.Dict[str, CatalogNode]
    errors: typing.Union[typing.List[str], None]


class Sources(Artifact, pydantic.BaseModel):
    """The sources artifact. """

    metadata: Metadata
    results: typing.List[SourcesFreshnessResult]
    elapsed_time: float


class Metadata(pydantic.BaseModel):
    """Data about the context in which the artifact was generated.
    
    Attributes:
        generated_at: The generated_at attribute
        invocation_id: The invocation_id attribute
        env: The env attribute
        project_id: The project_id attribute
        user_id: The user_id attribute
        send_anonymous_usage_stats: The send_anonymous_usage_stats attribute
        adapter_type: The adapter_type attribute

    """
    
    dbt_schema_version_raw: str
    dbt_version_raw: str
    generated_at: datetime.datetime
    invocation_id: uuid.UUID
    env: dict
    project_id: typing.Union[str, None]
    user_id: typing.Union[str, None]
    send_anonymous_usage_stats: typing.Union[bool, None]
    adapter_type: typing.Union[str, None]

    class Config:
        fields = {
            'dbt_version_raw': 'dbt_version',
            'dbt_schema_version_raw': 'dbt_schema_version',
        }

    @property
    def dbt_schema_version(self) -> int:
        """The artifact's schema version. 
        
        See https://schemas.getdbt.com for details.
        """

        return int(self.dbt_schema_version_raw.split('/')[-1].split('.')[0][1])

    @property
    def dbt_version(self) -> str:
        """The dbt version that generated the artifact.
        """

        return packaging.version.Version(self.dbt_version_raw)


class TimingResult(pydantic.BaseModel):
    """Timing details from running the node. """

    name: str
    started_at: typing.Union[None, datetime.datetime]
    completed_at: typing.Union[None, datetime.datetime]


class SourcesFreshnessResult(ArtifactNodeReader, pydantic.BaseModel):
    """Result details from checking the freshness of a source. """

    unique_id: str
    status: str
    error: typing.Union[None, str]
    max_loaded_at: typing.Union[None, str]
    snapshotted_at: typing.Union[None, str]
    max_loaded_at_time_ago_in_s: typing.Union[None, float]
    criteria: typing.Union[None, dict]  # TODO deserialize
    adapter_response: typing.Union[None, dict]
    timing: typing.Union[None,typing.List[TimingResult]]
    thread_id: typing.Union[None, str]
    execution_time: typing.Union[None, float]


class RunResultNode(ArtifactNodeReader, pydantic.BaseModel):
    """Details about the results of running a specific model, test, etc.
    """

    status: str
    timing: typing.List[TimingResult]
    thread_id: str
    execution_time: float
    adapter_response: dict
    message: typing.Union[str, None]
    failures: typing.Union[int, None]
    unique_id: str


class ManifestNode(ArtifactNodeReader, pydantic.BaseModel):
    """
    An object representing a node, such as a model, test, or macro.

    Attributes:
        raw_sql: the raw_sql attribute
        compiled: the compiled attribute
        database: the database attribute
        db_schema: the db_schema attribute
        fqn: the fqn attribute
        unique_id: the unique_id attribute
        package_name: the package_name attribute
        root_path: the root_path attribute
        path: the path attribute
        original_file_path: the original_file_path attribute
        name: the name attribute
        resource_type: the resource_type attribute
        alias: the alias attribute
        checksum: the checksum attribute
        config: the config attribute
        tags: the tags attribute
        refs: the refs attribute
        sources: the sources attribute
        depends_on: the depends_on attribute
        description: the description attribute
        columns: the columns attribute
        meta: the meta attribute
        docs: the docs attribute
        patch_path: the patch_path attribute
        compiled_path: the compiled_path attribute
        build_path: the build_path attribute
        deferred: the deferred attribute
        unrendered_config: the unrendered_config attribute
        created_at: the created_at attribute
        config_call_dict: the config_call_dict attribute
        compiled_sql: the compiled_sql attribute
        extra_ctes_injected: the extra_ctes_injected attribute
        extra_ctes: the extra_ctes attribute
        relation_name: the relation_name attribute
        column_name: the column_name attribute
        file_key_name: the file_key_name attribute

    """

    raw_sql: str
    compiled: typing.Union[str, None]
    database: typing.Union[str, None]
    db_schema: str
    fqn: typing.List[str]
    unique_id: str
    package_name: str
    root_path: str
    path: str
    original_file_path: str
    name: str
    resource_type: str
    alias: str
    checksum: dict
    config: typing.Union[None, typing.Dict]
    tags: typing.Union[None, typing.List[str]]
    refs: typing.Union[None, typing.List]
    sources: typing.Union[None, typing.List[typing.List[str]]]
    depends_on: typing.Union[None, typing.Dict]
    description: typing.Union[None, str]
    columns: typing.Union[None, typing.Dict]
    meta: typing.Union[None, typing.Dict]
    docs: typing.Union[None, typing.Dict]
    patch_path: typing.Union[None, str]
    compiled_path: typing.Union[None, str]
    build_path: typing.Union[None, str]
    deferred: typing.Union[None, bool]
    unrendered_config: typing.Union[None, dict]
    created_at: typing.Union[None, float]
    config_call_dict: typing.Union[None, dict]
    compiled_sql: typing.Union[None, str]
    extra_ctes_injected: typing.Union[None, bool]
    extra_ctes: typing.Union[None, typing.List[typing.Dict]]
    relation_name: typing.Union[None, str]
    column_name: typing.Union[None, str]  # only for generic test node
    file_key_name: typing.Union[None, str]  # only for generic test node

    class Config:
        fields = {
            'db_schema': 'schema',
        }


class ManifestNodeReference(ArtifactNodeReader):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if not isinstance(value, str):
            raise TypeError('ManifestNodeReferences must be strings')
        return cls(value)

    def __init__(self, unique_id: str):
        self.unique_id = unique_id
    
    def __repr__(self):
        return f"<ManifestNodeReference {self.unique_id}>"

    @property
    def resource_type(self) -> str:
        """
        The type of resource this reference points to. Eg model, test, source, etc.
        """

        return self.unique_id.split('.')[0]

    @property
    def node(self) -> ManifestNode:
        """
        The node this reference points to. 
        """

        if self.resource_type in ['seed', 'test', 'operation', 'model', 'snapshot']:
            return self.manifest_artifact.nodes[self.unique_id]
        elif self.resource_type == 'source':
            return self.manifest_artifact.sources[self.unique_id]
        elif self.resource_type == 'macro':
            return self.manifest_artifact.macros[self.unique_id]
        elif self.resource_type == 'exposure':
            return self.manifest_artifact.exposures[self.unique_id]
        elif self.resource_type == 'metric':
            return self.manifest_artifact.metrics[self.unique_id]
        elif self.resource_type == 'selector':
            return self.manifest_artifact.selectors[self.unique_id]
        else:
            raise AttributeError(f"Unknown resource type: {self.resource_type}")


class ManifestSourceNode(ArtifactNodeReader, pydantic.BaseModel):
    """Details about a Source node. """

    fqn: typing.List[str]
    database: typing.Union[None, str]
    db_schema: str
    unique_id: str
    package_name: str
    root_path: str
    path: str
    original_file_path: str
    name: str
    source_name: str
    source_description: str
    loader: str
    identifier: str
    resource_type: str
    quoting: typing.Union[dict, None]  # TODO deserialize
    loaded_at_field: typing.Union[None, str]
    freshness: typing.Union[None, dict]  # TODO deserialize
    external: typing.Union[None, dict]  # TODO deserialize
    description: typing.Union[None, str]
    columns: typing.Union[None, dict]  # TODO deserialize
    meta: typing.Union[dict]
    source_meta: typing.Union[dict]
    tags: typing.Union[typing.List[str]]
    config: typing.Union[dict]  # TODO deserialize
    patch_path: typing.Union[str, None]
    unrendered_config: typing.Union[dict, None]
    relation_name: typing.Union[str, None]
    created_at: typing.Union[None, float]

    class Config:
        fields = {
            'db_schema': 'schema',
        }


class ManifestMacroNode(pydantic.BaseModel):
    """Details about a Macro node. """

    unique_id: str
    package_name: str
    root_path: str
    path: str
    original_file_path: str
    name: str
    macro_sql: str
    resource_type: str
    tags: typing.Union[None, typing.List[str]]
    patch_path: typing.Union[None, str]
    created_at: typing.Union[None, float]
    description: typing.Union[None, str]
    meta: typing.Union[None, dict]
    docs: typing.Union[None, dict]  # TODO deserialize
    arguments: typing.Union[None, typing.List[typing.Dict]]  # TODO deserialize
    depends_on: typing.Union[None, typing.Dict[str, typing.List[str]]]  # TODO deserialize


class ManifestDocsNode(pydantic.BaseModel):
   """Details about a Docs node. """

   unique_id: str
   package_name: str
   root_path: str
   path: str
   original_filepath: typing.Union[str, None]
   name: str
   block_contents: str


class ManifestExposureNode(pydantic.BaseModel):
    """Details about an Exposure node.
    """

    fqn: str
    unique_id: str
    package_name: str
    root_path: str
    path: str
    original_file_path: str
    name: str
    node_type: str
    owner: str
    resource_type: typing.Union[str, None]
    description: typing.Union[str, None]
    maturity: typing.Union[str, None]
    meta: typing.Union[dict, None]
    tags: typing.Union[typing.List[str], None]
    url: typing.Union[str, None]
    refs: typing.Union[typing.List[list], None]
    sources: typing.Union[typing.List[list], None]
    created_at: typing.Union[float, None]
    depends_on: typing.Union[typing.Dict[str, list]]  # TODO deserialize

    class Config:
        fields = {
            'db_schema': 'schema',
            'node_type': 'type'
        }


class ManifestMetricNode(pydantic.BaseModel):
    """Details about a Metric node. """

    fqn: str
    unique_id: str
    package_name: str
    root_path: str
    path: str
    original_file_path: str
    model: str
    name: str
    description: str
    label: str
    node_type: str
    filters: typing.List[dict]  # TODO deserialize
    time_grains: typing.List[str]
    dimensions: typing.List[str]
    sql: typing.Union[str, None]
    timestamp: typing.Union[str, None]
    resource_type: typing.Union[str, None]
    meta: typing.Union[dict, None]
    tags: typing.Union[list, None]
    sources: typing.Union[typing.List[str], None]
    refs: typing.Union[typing.List[str], None]
    created_at: typing.Union[float, None]
    depends_on: typing.Union[dict, None]  # TODO deserialize

    class Config:
        fields = {
            'node_type': 'type'
        }

class CatalogNode(ArtifactNodeReader, pydantic.BaseModel):
    """Details about a Catalog node. """

    metadata: CatalogNodeMetadata
    columns: typing.Dict[str, CatalogNodeColumn]
    stats: typing.Dict[str, CatalogNodeStats]
    unique_id: str


class CatalogNodeMetadata(pydantic.BaseModel):
    """Metadata details about a CatalogNode. """

    node_type: str
    db_schema: str
    name: str
    database: typing.Union[str, None]
    comment: typing.Union[str, None]
    owner: typing.Union[str, None]

    class Config:
        fields = {
            'db_schema': 'schema',
            'node_type': 'type'
        }


class CatalogNodeColumn(pydantic.BaseModel):
    """Details about the columns in a CatalogNode. """

    node_type: str
    index: int
    name: str
    comment: typing.Union[str, None]

    class Config:
        fields = {
            'node_type': 'type'
        }


class CatalogNodeStats(pydantic.BaseModel):
    """Statics about a CatalogNode. 
    
    Attributes:
        description: The description of the statistic
        id: The id of the statistic
        include: TODO
        label: The label of the statistic
        value: The value of the statistic
    """

    description: typing.Union[str, None]
    id: str
    include: bool
    label: str
    value: typing.Union[str, None]


RunResults.update_forward_refs()
Manifest.update_forward_refs()
Catalog.update_forward_refs()
Sources.update_forward_refs()
CatalogNode.update_forward_refs()

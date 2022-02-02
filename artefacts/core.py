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


Metadata = typing.ForwardRef('Metadata')
RunResults = typing.ForwardRef('RunResults')
Catalog = typing.ForwardRef('Catalog')
Sources = typing.ForwardRef('Sources')
Manifest = typing.ForwardRef('Manifest')
ManifestNode = typing.ForwardRef('ManifestNode')
ManifestSourceNode = typing.ForwardRef('ManifestSourceNode')
ManifestMacroNode = typing.ForwardRef('ManifestMacroNode')
ManifestDocsNode = typing.ForwardRef('ManifestDocsNode')
ManifestExposureNode = typing.ForwardRef('ManifestExposureNode')
ManifestMetricNode = typing.ForwardRef('ManifestMetricNode')
RunResultNode = typing.ForwardRef('RunResultNode')
CatalogNode = typing.ForwardRef('CatalogNode')
CatalogNodeMetadata = typing.ForwardRef('CatalogNodeMetadata')
CatalogNodeColumn = typing.ForwardRef('CatalogNodeColumn')
CatalogNodeStats = typing.ForwardRef('CatalogNodeStats')
SourcesFreshnessResult = typing.ForwardRef('SourcesFreshnessResult')
ResultTiming = typing.ForwardRef('ResultTiming')


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

        return self.manifest_artifact.nodes.get(self.unique_id)

    @property
    def catalog(self):
        """A reference to details about the node contained in the catalog."""

        return self.catalog_artifact.nodes.get(self.unique_id)

    @property
    def run_results(self):
        """A reference to results from running the node, if it exists."""

        return [r for r in self.run_results_artifact.results if r.unique_id == self.unique_id]


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
    parent_map: typing.Union[dict, None]
    child_map: typing.Union[dict, None]


class RunResults(Artifact, pydantic.BaseModel):
    """The run_results artifact. 
    
    Attributes:
        metadata: The :class:`Metadata` associated with the run, such as when
                  the run was generated, the environment variables present
                  during the run, etc.
        results: A list of :class:`RunResultNode` s, which contain details 
                 about how long each node ran, whether it was successful, etc.
    
    """

    metadata: Metadata
    results: typing.List[RunResultNode]
    elapsed_time: float
    args: typing.Union[dict, None]


class Catalog(Artifact, pydantic.BaseModel):
    """The catalog artifact. """

    metadata: Metadata
    nodes: typing.Dict[str, CatalogNode]
    sources: typing.Dict[str, CatalogNode]
    errors: typing.Union[typing.List[str], None]


class Sources(Artifact, pydantic.BaseModel):
    """The sources artifact. """

    metadata: Metadata
    results: typing.List[dict]
    elapsed_time: float


class Metadata(pydantic.BaseModel):
    """Data about the context in which the artifact was generated."""
    
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
    def dbt_schema_version(self):
        return int(self.dbt_schema_version_raw.split('/')[-1].split('.')[0][1])

    @property
    def dbt_version(self):
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
    criteria: dict  # TODO deserialize
    adapter_response: dict
    timing: typing.List[TimingResult]
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

    class Config:
        fields = {
            'db_schema': 'schema',
        }


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

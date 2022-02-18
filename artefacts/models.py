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
from artefacts.mixins import ArtifactReader, ArtifactNodeReader


CatalogModel = typing.ForwardRef('CatalogModel')
CatalogNode = typing.ForwardRef('CatalogNode')
CatalogNodeColumn = typing.ForwardRef('CatalogNodeColumn')
CatalogNodeMetadata = typing.ForwardRef('CatalogNodeMetadata')
CatalogNodeStats = typing.ForwardRef('CatalogNodeStats')
ManifestModel = typing.ForwardRef('ManifestModel')
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
RunResultsModel = typing.ForwardRef('RunResultsModel')
SourcesModel = typing.ForwardRef('SourcesModel')
SourcesFreshnessResult = typing.ForwardRef('SourcesFreshnessResult')


class Deserializer(pydantic.BaseModel):
    
    def __repr__(self):
        return f"<{self.__class__.__name__}>"


class ManifestModel(Deserializer):
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

    # TODO: improve the way we validate minimum dbt versions.
    @pydantic.validator('metadata')
    def validate_metadata(cls, metadata):
        if metadata.dbt_version < packaging.version.parse('1.0'):
            raise ValueError(
                f"\n\tUnsupported dbt version: {metadata.dbt_version}. "
                "\n\tPlease upgrade dbt to at least v1.0 to use artefacts"
            )
        return metadata

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


class RunResultsModel(Deserializer):
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


class CatalogModel(Deserializer):
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


class SourcesModel(Deserializer):
    """The sources artifact. 
    
    Attributes:
        metadata: The metadata attribute
        results: The results attribute
        elapsed_time: The elapsed_time attribute

    """

    metadata: Metadata
    results: typing.List[SourcesFreshnessResult]
    elapsed_time: float


class Metadata(Deserializer):
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


class Quoting(Deserializer):
    """Details about quoting requirements for database objects

    Attributes:
        database: Whether to quote the "database" component of an object path
        identifier: Whether to quote the "identifier" component of an object path
        db_schema: Whether to quote the "db_schema" component of an object path
        column: Whether to quote the "column" component of an object path

    """
    
    database: typing.Union[bool, None]
    identifier: typing.Union[bool, None]
    db_schema: typing.Union[bool, None]
    column: typing.Union[bool, None]

    class Config:
        fields = {
            'db_schema': 'schema',
        }


class ExternalPartition(Deserializer):
    """
    Object representing a partition on an external table

    Attributes:
        name: The name attribute
        description: The description attribute
        data_type: The data_type attribute
        meta: The meta attribute
   
    """

    name: typing.Union[str, None]
    description: typing.Union[str, None]
    data_type: typing.Union[str, None]
    meta: typing.Union[dict, None]


class ExternalTable(Deserializer):
    """
    Object representing an external table

    Attributes:
        location: The location attribute
        file_format: The file_format attribute
        row_format: The row_format attribute
        tbl_properties: The tbl_properties attribute
        partitions: The partitions attribute

    """

    location: typing.Union[None, str]
    file_format: typing.Union[None, str]
    row_format: typing.Union[None, str]
    tbl_properties: typing.Union[None, str]
    partitions: typing.Union[typing.List[ExternalPartition], None]


class ColumnInfo(Deserializer):
    """Column details of a documented model

    Attributes:
        name: The name attribute
        description: The description attribute
        meta: The meta attribute
        data_type: The data_type attribute
        quote: The quote attribute
        tags: The tags attribute

    """

    name: str
    description: typing.Union[None, str]
    meta: typing.Union[None, dict]
    data_type: typing.Union[None, str]
    quote: typing.Union[None, bool]
    tags: typing.Union[None, typing.List[str]]


class TimingResult(Deserializer):
    """Timing details from running the node. 
    
    Attributes:
        name: the name attribute
        started_at: the started_at attribute
        completed_at: the completed_at attribute

    """

    name: str
    started_at: typing.Union[None, datetime.datetime]
    completed_at: typing.Union[None, datetime.datetime]


class SourceConfig(Deserializer):
    """An object containing details about a source's config

    Attributes:
        enabled: Whether the source is enabled
    """

    enabled: typing.Union[bool, None]


class Time(Deserializer):
    """An object representing a time interval, used for example when
    configuring a source freshness check

    Attributes:
        period: The length of the time interval, eg days, hours, seconds
        count: The number of periods associed with the time interval
    """

    count: typing.Union[int, None]
    period: typing.Union[str, None]


class FreshnessThreshold(Deserializer):
    """Details of the criteria used when checking a source's freshness

    Attributes:
        warn_after: The freshness criteria after which a freshness check will
                    raise a warning.
        error_after: The freshness criteria after which a freshness check will
                     raise an error.
        filter: A SQL statement used to filter the table when running a
                freshness check.
    """

    warn_after: typing.Union[Time, None]
    error_after: typing.Union[Time, None]
    filter: typing.Union[str, None]


class SourcesFreshnessResult(ArtifactNodeReader, Deserializer):
    """Result details from checking the freshness of a source. 
    
    Attributes:
        unique_id: The unique_id attribute
        status: The status attribute
        error: The error attribute
        max_loaded_at: The max_loaded_at attribute
        snapshotted_at: The snapshotted_at attribute
        max_loaded_at_time_ago_in_s: The max_loaded_at_time_ago_in_s attribute
        criteria: The criteria attribute
        adapter_response: The adapter_response attribute
        timing: The timing attribute
        thread_id: The thread_id attribute
        execution_time: The execution_time attribute

    """

    unique_id: str
    status: str
    error: typing.Union[None, str]
    max_loaded_at: typing.Union[None, str]
    snapshotted_at: typing.Union[None, str]
    max_loaded_at_time_ago_in_s: typing.Union[None, float]
    criteria: typing.Union[None, FreshnessThreshold]
    adapter_response: typing.Union[None, dict]
    timing: typing.Union[None,typing.List[TimingResult]]
    thread_id: typing.Union[None, str]
    execution_time: typing.Union[None, float]


class RunResultNode(ArtifactNodeReader, Deserializer):
    """Details about the results of running a specific model, test, etc.

    Attributes:
        status: The status attribute
        timing: The timing attribute
        thread_id: The thread_id attribute
        execution_time: The execution_time attribute
        adapter_response: The adapter_response attribute
        message: The message attribute
        failures: The failures attribute
        unique_id: The unique_id attribute

    """

    status: str
    timing: typing.List[TimingResult]
    thread_id: str
    execution_time: float
    adapter_response: dict
    message: typing.Union[str, None]
    failures: typing.Union[int, None]
    unique_id: str


class ManifestNode(ArtifactNodeReader, Deserializer):
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


class ManifestSourceNode(ArtifactNodeReader, Deserializer):
    """Details about a Source node. 
    
    Attributes:
        fqn: The fqn attribute
        database: The database attribute
        db_schema: The db_schema attribute
        unique_id: The unique_id attribute
        package_name: The package_name attribute
        root_path: The root_path attribute
        path: The path attribute
        original_file_path: The original_file_path attribute
        name: The name attribute
        source_name: The source_name attribute
        source_description: The source_description attribute
        loader: The loader attribute
        identifier: The identifier attribute
        resource_type: The resource_type attribute
        quoting: The quoting attribute
        loaded_at_field: The loaded_at_field attribute
        freshness: The freshness attribute
        external: The external attribute
        description: The description attribute
        columns: The columns attribute
        meta: The meta attribute
        source_meta: The source_meta attribute
        tags: The tags attribute
        config: The config attribute
        patch_path: The patch_path attribute
        unrendered_config: The unrendered_config attribute
        relation_name: The relation_name attribute
        created_at: The created_at attribute

    """

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
    quoting: typing.Union[Quoting, None]
    loaded_at_field: typing.Union[None, str]
    freshness: typing.Union[None, FreshnessThreshold]
    external: typing.Union[None, ExternalTable]
    description: typing.Union[None, str]
    columns: typing.Union[None, typing.Dict[str, ColumnInfo]]
    meta: typing.Union[dict]
    source_meta: typing.Union[dict]
    tags: typing.Union[typing.List[str]]
    config: typing.Union[SourceConfig, None]
    patch_path: typing.Union[str, None]
    unrendered_config: typing.Union[dict, None]
    relation_name: typing.Union[str, None]
    created_at: typing.Union[None, float]

    class Config:
        fields = {
            'db_schema': 'schema',
        }


class MacroArgument(Deserializer):
    """Details about the arguments of a macro

    Attributes:
        name: The name attribute
        type: The type attribute
        description: The description attribute

    """

    name: str
    type: typing.Union[str, None]
    description: typing.Union[str, None]


class ManifestMacroNode(Deserializer):
    """Details about a Macro node. 
    
    Attributes:
        unique_id: The unique_id attribute
        package_name: The package_name attribute
        root_path: The root_path attribute
        path: The path attribute
        original_file_path: The original_file_path attribute
        name: The name attribute
        macro_sql: The macro_sql attribute
        resource_type: The resource_type attribute
        tags: The tags attribute
        patch_path: The patch_path attribute
        created_at: The created_at attribute
        description: The description attribute
        meta: The meta attribute
        docs: The docs attribute
        arguments: The arguments attribute
        depends_on: The depends_on attribute

    """

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
    docs: typing.Union[None, dict]
    arguments: typing.Union[None, typing.List[MacroArgument]]
    depends_on: typing.Union[None, typing.Dict[str, typing.List[str]]]


class ManifestDocsNode(Deserializer):
    """Details about a Docs node. 

    Attributes:
        unique_id: The unique_id attribute
        package_name: The package_name attribute
        root_path: The root_path attribute
        path: The path attribute
        original_filepath: The original_filepath attribute
        name: The name attribute
        block_contents: The block_contents attribute

    """

    unique_id: str
    package_name: str
    root_path: str
    path: str
    original_filepath: typing.Union[str, None]
    name: str
    block_contents: str


class ManifestExposureNode(Deserializer):
    """Details about an Exposure node.

    Attributes:
        fqn: Details about a fqn attribute 
        unique_id: Details about a unique_id attribute 
        package_name: Details about a package_name attribute 
        root_path: Details about a root_path attribute 
        path: Details about a path attribute 
        original_file_path: Details about a original_file_path attribute 
        name: Details about a name attribute 
        node_type: Details about a node_type attribute 
        owner: Details about a owner attribute 
        resource_type: Details about a resource_type attribute 
        description: Details about a description attribute 
        maturity: Details about a maturity attribute 
        meta: Details about a meta attribute 
        tags: Details about a tags attribute 
        url: Details about a url attribute 
        refs: Details about a refs attribute 
        sources: Details about a sources attribute 
        created_at: Details about a created_at attribute 
        depends_on: Details about a depends_on attribute 

    """

    fqn: typing.List[str]
    unique_id: str
    package_name: str
    root_path: str
    path: str
    original_file_path: str
    name: str
    node_type: str
    owner: dict
    resource_type: typing.Union[str, None]
    description: typing.Union[str, None]
    maturity: typing.Union[str, None]
    meta: typing.Union[dict, None]
    tags: typing.Union[typing.List[str], None]
    url: typing.Union[str, None]
    refs: typing.Union[typing.List[list], None]
    sources: typing.Union[typing.List[list], None]
    created_at: typing.Union[float, None]
    depends_on: typing.Union[typing.Dict[str, list]]

    class Config:
        fields = {
            'db_schema': 'schema',
            'node_type': 'type'
        }


class MetricFilter(Deserializer):
    """Details about a Metric filter.

    Attributes:
        field: The field attribute
        operator: The operator attribute
        value: The value attribute
    """

    field: str
    operator: str
    value: str


class ManifestMetricNode(Deserializer):
    """Details about a Metric node. 

    Attributes:
        fqn: The fqn attribute
        unique_id: The unique_id attribute
        package_name: The package_name attribute
        root_path: The root_path attribute
        path: The path attribute
        original_file_path: The original_file_path attribute
        model: The model attribute
        name: The name attribute
        description: The description attribute
        label: The label attribute
        node_type: The node_type attribute
        filters: The filters attribute
        time_grains: The time_grains attribute
        dimensions: The dimensions attribute
        sql: The sql attribute
        timestamp: The timestamp attribute
        resource_type: The resource_type attribute
        meta: The meta attribute
        tags: The tags attribute
        sources: The sources attribute
        refs: The refs attribute
        created_at: The created_at attribute
        depends_on: The depends_on attribute

    """

    fqn: typing.List[str]
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
    filters: typing.List[MetricFilter]
    time_grains: typing.List[str]
    dimensions: typing.List[str]
    sql: typing.Union[str, None]
    timestamp: typing.Union[str, None]
    resource_type: typing.Union[str, None]
    meta: typing.Union[dict, None]
    tags: typing.Union[list, None]
    sources: typing.Union[typing.List[str], None]
    refs: typing.Union[typing.List[typing.List[str]], None]
    created_at: typing.Union[float, None]
    depends_on: typing.Union[dict, None]

    class Config:
        fields = {
            'node_type': 'type'
        }

class CatalogNode(ArtifactNodeReader, Deserializer):
    """Details about a Catalog node. 

    Attributes:
        metadata: The metadata attribute 
        columns: The columns attribute 
        stats: The stats attribute 
        unique_id: The unique_id attribute
    
    """

    metadata: CatalogNodeMetadata
    columns: typing.Dict[str, CatalogNodeColumn]
    stats: typing.Dict[str, CatalogNodeStats]
    unique_id: str


class CatalogNodeMetadata(Deserializer):
    """Metadata details about a CatalogNode. 

    Attributes:    
        node_type: The node_type attribute
        db_schema: The db_schema attribute
        name: The name attribute
        database: The database attribute
        comment: The comment attribute
        owner: The owner attribute

    """

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


class CatalogNodeColumn(Deserializer):
    """Details about the columns in a CatalogNode. 
    
    Attributes:
        node_type: The node_type attribute
        index: The index attribute
        name: The name attribute
        comment: The comment attribute
    
    """

    node_type: str
    index: int
    name: str
    comment: typing.Union[str, None]

    class Config:
        fields = {
            'node_type': 'type'
        }


class CatalogNodeStats(Deserializer):
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


RunResultsModel.update_forward_refs()
ManifestModel.update_forward_refs()
CatalogModel.update_forward_refs()
SourcesModel.update_forward_refs()
CatalogNode.update_forward_refs()

import datetime
import uuid
import pydantic
from typing import Union, Literal, Dict, List, Iterable, Optional
from typing_extensions import Annotated
import packaging.version

from artefacts.mixins import ArtifactNodeReader


class Model(pydantic.BaseModel):
    def __repr__(self):
        return f"<{self.__class__.__name__}>"

    def __getattr__(self, attr):
        raise AttributeError(
            f"{self.__class__.__name__} has no attribute '{attr}'.\n\n"
            f"Please see {self.__class__._docs_path()} for available attributes"
            f" of this model."
        )

    @classmethod
    def _qualpath(cls):
        return f"{cls.__module__}" + "." + f"{cls.__qualname__}"

    @classmethod
    def _docs_path(cls):
        return (
            f"https://tjwaterman99.github.io/artefacts/reference.html#{cls._qualpath()}"
        )


class ManifestModelNode(ArtifactNodeReader, Model):
    """
    An object representing a model in the dbt project.
    """

    class Config:
        fields = {
            "db_schema": "schema",
        }

    raw_sql: str
    """ The raw_sql attribute """

    compiled: Optional["str"]
    """ The compiled attribute """

    database: Optional["str"]
    """ The database attribute """

    db_schema: str
    """ The db_schema attribute """

    fqn: List[str]
    """ The fqn attribute """

    unique_id: str
    """ The unique_id attribute """

    package_name: str
    """ The package_name attribute """

    root_path: str
    """ The root_path attribute """

    path: str
    """ The path attribute """

    original_file_path: str
    """ The original_file_path attribute """

    name: str
    """ The name attribute """

    resource_type: Literal["model"]
    """ The resource_type attribute """

    alias: str
    """ The alias attribute """

    checksum: dict
    """ The checksum attribute """

    config: Optional[Dict]
    """ The config attribute """

    tags: Optional[List[str]]
    """ The tags attribute """

    refs: Optional[List]
    """ The refs attribute """

    sources: Optional[List[List[str]]]
    """ The sources attribute """

    depends_on: Optional[Dict]
    """ The depends_on attribute """

    description: Optional[str]
    """ The description attribute """

    columns: Optional[Dict]
    """ The columns attribute """

    meta: Optional[Dict]
    """ The meta attribute """

    docs: Optional[Dict]
    """ The docs attribute """

    patch_path: Optional[str]
    """ The patch_path attribute """

    compiled_path: Optional[str]
    """ The compiled_path attribute """

    build_path: Optional[str]
    """ The build_path attribute """

    deferred: Optional[bool]
    """ The deferred attribute """

    unrendered_config: Optional[dict]
    """ The unrendered_config attribute """

    created_at: Optional[float]
    """ The created_at attribute """

    config_call_dict: Optional[dict]
    """ The config_call_dict attribute """

    compiled_sql: Optional[str]
    """ The compiled_sql attribute """

    extra_ctes_injected: Optional[bool]
    """ The extra_ctes_injected attribute """

    extra_ctes: Optional[List[Dict]]
    """ The extra_ctes attribute """

    relation_name: Optional[str]
    """ The relation_name attribute """

    _test_path = "manifest.nodes['model.poffertjes_shop.products']"


class ManifestTestNode(ArtifactNodeReader, Model):
    """
    An object representing a test in the dbt project.
    """

    class Config:
        fields = {
            "db_schema": "schema",
        }

    raw_sql: str
    "The raw_sql attribute"

    compiled: Optional["str"]
    "The compiled attribute"

    database: Optional["str"]
    "The database attribute"

    db_schema: str
    "The db_schema attribute"

    fqn: List[str]
    "The fqn attribute"

    unique_id: str
    "The unique_id attribute"

    package_name: str
    "The package_name attribute"

    root_path: str
    "The root_path attribute"

    path: str
    "The path attribute"

    original_file_path: str
    "The original_file_path attribute"

    name: str
    "The name attribute"

    resource_type: Literal["test"]
    "The resource_type attribute"

    alias: str
    "The alias attribute"

    checksum: dict
    "The checksum attribute"

    config: Optional[Dict]
    "The config attribute"

    tags: Optional[List[str]]
    "The tags attribute"

    refs: Optional[List]
    "The refs attribute"

    sources: Optional[List[List[str]]]
    "The sources attribute"

    depends_on: Optional[Dict]
    "The depends_on attribute"

    description: Optional[str]
    "The description attribute"

    columns: Optional[Dict]
    "The columns attribute"

    meta: Optional[Dict]
    "The meta attribute"

    docs: Optional[Dict]
    "The docs attribute"

    patch_path: Optional[str]
    "The patch_path attribute"

    compiled_path: Optional[str]
    "The compiled_path attribute"

    build_path: Optional[str]
    "The build_path attribute"

    deferred: Optional[bool]
    "The deferred attribute"

    unrendered_config: Optional[dict]
    "The unrendered_config attribute"

    created_at: Optional[float]
    "The created_at attribute"

    config_call_dict: Optional[dict]
    "The config_call_dict attribute"

    compiled_sql: Optional[str]
    "The compiled_sql attribute"

    extra_ctes_injected: Optional[bool]
    "The extra_ctes_injected attribute"

    extra_ctes: Optional[List[Dict]]
    "The extra_ctes attribute"

    relation_name: Optional[str]
    "The relation_name attribute"

    _test_path = (
        "manifest.nodes['test.poffertjes_shop.not_null_base_"
        "customers_customer_id.59e00b9238']"
    )


class ManifestOperationNode(ArtifactNodeReader, Model):
    """
    An object representing a macro operation in the dbt project.
    """

    class Config:
        fields = {
            "db_schema": "schema",
        }

    raw_sql: str
    """The raw_sql attribute"""

    compiled: Optional["str"]
    """The compiled attribute"""

    database: Optional["str"]
    """The database attribute"""

    db_schema: str
    """The db_schema attribute"""

    fqn: List[str]
    """The fqn attribute"""

    unique_id: str
    """The unique_id attribute"""

    package_name: str
    """The package_name attribute"""

    root_path: str
    """The root_path attribute"""

    path: str
    """The path attribute"""

    original_file_path: str
    """The original_file_path attribute"""

    name: str
    """The name attribute"""

    resource_type: Literal["operation"]
    """The resource_type attribute"""

    alias: str
    """The alias attribute"""

    checksum: dict
    """The checksum attribute"""

    config: Optional[Dict]
    """The config attribute"""

    tags: Optional[List[str]]
    """The tags attribute"""

    refs: Optional[List]
    """The refs attribute"""

    sources: Optional[List[List[str]]]
    """The sources attribute"""

    depends_on: Optional[Dict]
    """The depends_on attribute"""

    description: Optional[str]
    """The description attribute"""

    columns: Optional[Dict]
    """The columns attribute"""

    meta: Optional[Dict]
    """The meta attribute"""

    docs: Optional[Dict]
    """The docs attribute"""

    patch_path: Optional[str]
    """The patch_path attribute"""

    compiled_path: Optional[str]
    """The compiled_path attribute"""

    build_path: Optional[str]
    """The build_path attribute"""

    deferred: Optional[bool]
    """The deferred attribute"""

    unrendered_config: Optional[dict]
    """The unrendered_config attribute"""

    created_at: Optional[float]
    """The created_at attribute"""

    config_call_dict: Optional[dict]
    """The config_call_dict attribute"""

    compiled_sql: Optional[str]
    """The compiled_sql attribute"""

    extra_ctes_injected: Optional[bool]
    """The extra_ctes_injected attribute"""

    extra_ctes: Optional[List[Dict]]
    """The extra_ctes attribute"""

    relation_name: Optional[str]
    """The relation_name attribute"""

    _test_path = (
        "manifest.nodes['operation.poffertjes_shop.poffertjes_" "shop-on-run-start-0']"
    )


class ManifestSnapshotNode(ArtifactNodeReader, Model):
    """
    An object representing a snapshot in the dbt project.
    """

    class Config:
        fields = {
            "db_schema": "schema",
        }

    raw_sql: str
    """ The raw_sql attribute """

    compiled: Optional["str"]
    """ The compiled attribute """

    database: Optional["str"]
    """ The database attribute """

    db_schema: str
    """ The db_schema attribute """

    fqn: List[str]
    """ The fqn attribute """

    unique_id: str
    """ The unique_id attribute """

    package_name: str
    """ The package_name attribute """

    root_path: str
    """ The root_path attribute """

    path: str
    """ The path attribute """

    original_file_path: str
    """ The original_file_path attribute """

    name: str
    """ The name attribute """

    resource_type: Literal["snapshot"]
    """ The resource_type attribute """

    alias: str
    """ The alias attribute """

    checksum: dict
    """ The checksum attribute """

    config: Optional[Dict]
    """ The config attribute """

    tags: Optional[List[str]]
    """ The tags attribute """

    refs: Optional[List]
    """ The refs attribute """

    sources: Optional[List[List[str]]]
    """ The sources attribute """

    depends_on: Optional[Dict]
    """ The depends_on attribute """

    description: Optional[str]
    """ The description attribute """

    columns: Optional[Dict]
    """ The columns attribute """

    meta: Optional[Dict]
    """ The meta attribute """

    docs: Optional[Dict]
    """ The docs attribute """

    patch_path: Optional[str]
    """ The patch_path attribute """

    compiled_path: Optional[str]
    """ The compiled_path attribute """

    build_path: Optional[str]
    """ The build_path attribute """

    deferred: Optional[bool]
    """ The deferred attribute """

    unrendered_config: Optional[dict]
    """ The unrendered_config attribute """

    created_at: Optional[float]
    """ The created_at attribute """

    config_call_dict: Optional[dict]
    """ The config_call_dict attribute """

    compiled_sql: Optional[str]
    """ The compiled_sql attribute """

    extra_ctes_injected: Optional[bool]
    """ The extra_ctes_injected attribute """

    extra_ctes: Optional[List[Dict]]
    """ The extra_ctes attribute """

    relation_name: Optional[str]
    """ The relation_name attribute """

    _test_path = "manifest.nodes['snapshot.poffertjes_shop.orders_snapshot']"


class ManifestSeedNode(ArtifactNodeReader, Model):
    """
    An object representing a seed in the dbt project.
    """

    class Config:
        fields = {
            "db_schema": "schema",
        }

    raw_sql: str
    """ The raw_sql attribute """

    compiled: Optional["str"]
    """ The compiled attribute """

    database: Optional["str"]
    """ The database attribute """

    db_schema: str
    """ The db_schema attribute """

    fqn: List[str]
    """ The fqn attribute """

    unique_id: str
    """ The unique_id attribute """

    package_name: str
    """ The package_name attribute """

    root_path: str
    """ The root_path attribute """

    path: str
    """ The path attribute """

    original_file_path: str
    """ The original_file_path attribute """

    name: str
    """ The name attribute """

    resource_type: Literal["seed"]
    """ The resource_type attribute """

    alias: str
    """ The alias attribute """

    checksum: dict
    """ The checksum attribute """

    config: Optional[Dict]
    """ The config attribute """

    tags: Optional[List[str]]
    """ The tags attribute """

    refs: Optional[List]
    """ The refs attribute """

    sources: Optional[List[List[str]]]
    """ The sources attribute """

    depends_on: Optional[Dict]
    """ The depends_on attribute """

    description: Optional[str]
    """ The description attribute """

    columns: Optional[Dict]
    """ The columns attribute """

    meta: Optional[Dict]
    """ The meta attribute """

    docs: Optional[Dict]
    """ The docs attribute """

    patch_path: Optional[str]
    """ The patch_path attribute """

    compiled_path: Optional[str]
    """ The compiled_path attribute """

    build_path: Optional[str]
    """ The build_path attribute """

    deferred: Optional[bool]
    """ The deferred attribute """

    unrendered_config: Optional[dict]
    """ The unrendered_config attribute """

    created_at: Optional[float]
    """ The created_at attribute """

    config_call_dict: Optional[dict]
    """ The config_call_dict attribute """

    compiled_sql: Optional[str]
    """ The compiled_sql attribute """

    extra_ctes_injected: Optional[bool]
    """ The extra_ctes_injected attribute """

    extra_ctes: Optional[List[Dict]]
    """ The extra_ctes attribute """

    relation_name: Optional[str]
    """ The relation_name attribute """

    _test_path = "manifest.nodes['seed.poffertjes_shop.shoppes']"


class ManifestAnalysisNode(ArtifactNodeReader, Model):
    """
    An object representing an analysis in the dbt project.
    """

    class Config:
        fields = {
            "db_schema": "schema",
        }

    raw_sql: str
    """ The raw_sql attribute """

    compiled: Optional["str"]
    """ The compiled attribute """

    database: Optional["str"]
    """ The database attribute """

    db_schema: str
    """ The db_schema attribute """

    fqn: List[str]
    """ The fqn attribute """

    unique_id: str
    """ The unique_id attribute """

    package_name: str
    """ The package_name attribute """

    root_path: str
    """ The root_path attribute """

    path: str
    """ The path attribute """

    original_file_path: str
    """ The original_file_path attribute """

    name: str
    """ The name attribute """

    resource_type: Literal["analysis"]
    """ The resource_type attribute """

    alias: str
    """ The alias attribute """

    checksum: dict
    """ The checksum attribute """

    config: Optional[Dict]
    """ The config attribute """

    tags: Optional[List[str]]
    """ The tags attribute """

    refs: Optional[List]
    """ The refs attribute """

    sources: Optional[List[List[str]]]
    """ The sources attribute """

    depends_on: Optional[Dict]
    """ The depends_on attribute """

    description: Optional[str]
    """ The description attribute """

    columns: Optional[Dict]
    """ The columns attribute """

    meta: Optional[Dict]
    """ The meta attribute """

    docs: Optional[Dict]
    """ The docs attribute """

    patch_path: Optional[str]
    """ The patch_path attribute """

    compiled_path: Optional[str]
    """ The compiled_path attribute """

    build_path: Optional[str]
    """ The build_path attribute """

    deferred: Optional[bool]
    """ The deferred attribute """

    unrendered_config: Optional[dict]
    """ The unrendered_config attribute """

    created_at: Optional[float]
    """ The created_at attribute """

    config_call_dict: Optional[dict]
    """ The config_call_dict attribute """

    compiled_sql: Optional[str]
    """ The compiled_sql attribute """

    extra_ctes_injected: Optional[bool]
    """ The extra_ctes_injected attribute """

    extra_ctes: Optional[List[Dict]]
    """ The extra_ctes attribute """

    relation_name: Optional[str]
    """ The relation_name attribute """

    _test_path = "manifest.nodes['analysis.poffertjes_shop.poffertjes_per_person']"


ManifestModelUnion = Union[
    ManifestModelNode,
    ManifestTestNode,
    ManifestOperationNode,
    ManifestSnapshotNode,
    ManifestSeedNode,
    ManifestAnalysisNode,
]

ManifestNode = Annotated[
    ManifestModelUnion, pydantic.Field(discriminator="resource_type")
]


class ManifestModel(Model):
    """
    The manifest artifact.
    """

    _test_path = "manifest"

    # TODO: improve the way we validate minimum dbt versions. We should
    # probably do the validation on every artifact.
    @pydantic.validator("metadata")
    def validate_metadata(cls, metadata):
        if metadata.dbt_version < packaging.version.parse("1.0"):
            raise ValueError(
                f"\n\tUnsupported dbt version: {metadata.dbt_version}. "
                "\n\tPlease upgrade dbt to at least v1.0 to use artefacts"
            )
        return metadata

    class Config:
        arbitrary_types_allowed = True
        fields = {
            "raw_disabled": "disabled",
        }

    metadata: "Metadata"
    """ The metadata attribute """

    nodes: Dict[str, ManifestNode]
    """ The nodes attribute """

    sources: Dict[str, "ManifestSourceNode"]
    """ The sources attribute """

    macros: Dict[str, "ManifestMacroNode"]
    """ The macros attribute """

    docs: Dict[str, "ManifestDocsNode"]
    """ The docs attribute """

    exposures: Dict[str, "ManifestExposureNode"]
    """ The exposures attribute """

    metrics: Dict[str, "ManifestMetricNode"]
    """ The metrics attribute """

    selectors: dict
    """ The selectors attribute """

    raw_disabled: Dict[str, List[ManifestModelUnion]]
    """ The disabled attribute """

    parent_map: Optional[Dict[str, List["ManifestNodeReference"]]]
    """ The parent_map attribute """

    child_map: Optional[Dict[str, List["ManifestNodeReference"]]]
    """ The child_map attribute """

    @property
    def resources(self) -> Dict:
        """A dictionary containing all resources defined in the dbt project"""

        return {
            **self.nodes,
            **self.sources,
            **self.macros,
            **self.exposures,
            **self.metrics,
            **self.disabled,
        }

    @property
    def disabled(self) -> Dict:
        """A dictionary containing all disabled resources defined in the dbt project

        See the discussion on Github for some caveats:
        https://github.com/tjwaterman99/artefacts/issues/89
        """

        return {k: v[0] for k, v in self.raw_disabled.items()}

    def iter_resource_type(
        self,
        resource_type: str,
        package_name: str = None,
        include_disabled: bool = False,
    ) -> Iterable:
        """Iterate over all resources of a specific type

        Args:
            resource_type (str): The type of resource, eg 'model', 'source',
                                 'exposure', etc.
            package_name (str): Only return resources from the specified dbt package.
            include_disabled: (bool): Include disabled resources. Default `False`.
        """

        for k, v in self.resources.items():
            if package_name and v.package_name != package_name:
                continue
            if v.disabled and include_disabled is False:
                continue
            if v.resource_type == resource_type:
                yield v


class RunResultsModel(Model):
    """The run_results artifact."""

    _test_path = "run_results"

    metadata: "Metadata"
    """ The metadata attribute """

    results: List["RunResultNode"]
    """ The results attribute """

    elapsed_time: float
    """ The elapsed_time attribute """

    args: Optional[Dict]
    """ The args attribute """


class CatalogModel(Model):
    """The catalog artifact."""

    _test_path = "catalog"

    metadata: "Metadata"
    """ The metadata attribute """

    nodes: Dict[str, "CatalogNode"]
    """ The nodes attribute """

    sources: Dict[str, "CatalogNode"]
    """ The sources attribute """

    errors: Optional[List[str]]
    """ The errors attribute """


class SourcesModel(Model):
    """The sources artifact."""

    _test_path = "sources"

    metadata: "Metadata"
    """ The metadata attribute """

    results: List["SourcesFreshnessResult"]
    """ The results attribute """

    elapsed_time: float
    """ The elapsed_time attribute """


class Metadata(Model):
    """Data about the context in which the artifact was generated."""

    _test_path = "manifest.metadata"

    dbt_schema_version_raw: str
    """ The dbt_schema_version_raw attribute """

    dbt_version_raw: str
    """ The dbt_version_raw attribute """

    generated_at: datetime.datetime
    """ The generated_at attribute """

    invocation_id: uuid.UUID
    """ The invocation_id attribute """

    env: dict
    """ The env attribute """

    project_id: Optional["str"]
    """ The project_id attribute """

    user_id: Optional["str"]
    """ The user_id attribute """

    send_anonymous_usage_stats: Optional[bool]
    """ The send_anonymous_usage_stats attribute """

    adapter_type: Optional["str"]
    """ The adapter_type attribute """

    class Config:
        fields = {
            "dbt_version_raw": "dbt_version",
            "dbt_schema_version_raw": "dbt_schema_version",
        }

    @property
    def dbt_schema_version(self) -> int:
        """The artifact's schema version.

        See https://schemas.getdbt.com for details.
        """

        return int(self.dbt_schema_version_raw.split("/")[-1].split(".")[0][1])

    @property
    def dbt_version(self) -> packaging.version.Version:
        """The dbt version that generated the artifact."""

        return packaging.version.Version(self.dbt_version_raw)


class Quoting(Model):
    """Details about quoting requirements for database objects

    Attributes:
        database: Whether to quote the "database" component of an object path
        identifier: Whether to quote the "identifier" component of an object path
        db_schema: Whether to quote the "db_schema" component of an object path
        column: Whether to quote the "column" component of an object path

    """

    _test_path = 'manifest.sources["source.poffertjes_shop.raw.orders"].quoting'

    database: Optional[bool]
    """ The database attribute """

    identifier: Optional[bool]
    """ The identifier attribute """

    db_schema: Optional[bool]
    """ The db_schema attribute """

    column: Optional[bool]
    """ The column attribute """

    class Config:
        fields = {
            "db_schema": "schema",
        }


class ExternalPartition(Model):
    """
    Object representing a partition on an external table
    """

    _test_path = (
        "manifest.sources['source.poffertjes_shop.raw.external_events']"
        ".external.partitions[0]"
    )

    name: Optional["str"]
    """ The name attribute """

    description: Optional["str"]
    """ The description attribute """

    data_type: Optional["str"]
    """ The data_type attribute """

    meta: Optional[Dict]
    """ The meta attribute """


class ExternalTable(Model):
    """
    Object representing an external table
    """

    _test_path = (
        "manifest.sources['source.poffertjes_shop.raw.external_events'].external"
    )

    location: Optional[str]
    """ The location attribute """

    file_format: Optional[str]
    """ The file_format attribute """

    row_format: Optional[str]
    """ The row_format attribute """

    tbl_properties: Optional[str]
    """ The tbl_properties attribute """

    partitions: Optional[List[ExternalPartition]]
    """ The partitions attribute """


class ColumnInfo(Model):
    """Column details of a documented model"""

    _test_path = (
        "manifest.sources['source.poffertjes_shop.raw.orders'].columns['order_id']"
    )

    name: str
    """ The name attribute """

    description: Optional[str]
    """ The description attribute """

    meta: Optional[dict]
    """ The meta attribute """

    data_type: Optional[str]
    """ The data_type attribute """

    quote: Optional[bool]
    """ The quote attribute """

    tags: Optional[List[str]]
    """ The tags attribute """


class TimingResult(Model):
    """Timing details from running the node.

    Attributes:
        name: the name attribute
        started_at: the started_at attribute
        completed_at: the completed_at attribute

    """

    _test_path = "sources.results[0].timing[0]"

    name: str
    """ The name attribute """

    started_at: Optional[datetime.datetime]
    """ The started_at attribute """

    completed_at: Optional[datetime.datetime]
    """ The completed_at attribute """


class SourceConfig(Model):
    """An object containing details about a source's config"""

    _test_path = "manifest.sources['source.poffertjes_shop.raw.products'].config"

    enabled: Optional[bool]
    """ The enabled attribute """


class Time(Model):
    """An object representing a time interval, used for example when
    configuring a source freshness check
    """

    _test_path = (
        "manifest.sources['source.poffertjes_shop.raw.products'].freshness.error_after"
    )

    count: Optional[int]
    """ The count attribute """

    period: Optional["str"]
    """ The period attribute """


class FreshnessThreshold(Model):
    """Details of the criteria used when checking a source's freshness"""

    _test_path = "manifest.sources['source.poffertjes_shop.raw.products'].freshness"

    warn_after: Optional[Time]
    """ The warn_after attribute """

    error_after: Optional[Time]
    """ The error_after attribute """

    filter: Optional["str"]
    """ The filter attribute """


class SourcesFreshnessResult(ArtifactNodeReader, Model):
    """Result details from checking the freshness of a source."""

    _test_path = "sources.results[0]"

    unique_id: str
    """ The unique_id attribute """

    status: str
    """ The status attribute """

    error: Optional[str]
    """ The error attribute """

    max_loaded_at: Optional[str]
    """ The max_loaded_at attribute """

    snapshotted_at: Optional[str]
    """ The snapshotted_at attribute """

    max_loaded_at_time_ago_in_s: Optional[float]
    """ The max_loaded_at_time_ago_in_s attribute """

    criteria: Optional[FreshnessThreshold]
    """ The criteria attribute """

    adapter_response: Optional[dict]
    """ The adapter_response attribute """

    timing: Optional[List[TimingResult]]
    """ The timing attribute """

    thread_id: Optional[str]
    """ The thread_id attribute """

    execution_time: Optional[float]
    """ The execution_time attribute """


class RunResultNode(ArtifactNodeReader, Model):
    """Details about the results of running a specific model, test, etc."""

    _test_path = "run_results.results[0]"

    status: str
    """ The status attribute """

    timing: List[TimingResult]
    """ The timing attribute """

    thread_id: str
    """ The thread_id attribute """

    execution_time: float
    """ The execution_time attribute """

    adapter_response: dict
    """ The adapter_response attribute """

    message: Optional["str"]
    """ The message attribute """

    failures: Optional[int]
    """ The failures attribute """

    unique_id: str
    """ The unique_id attribute """


class ManifestNodeReference(ArtifactNodeReader):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if not isinstance(value, str):
            raise TypeError("ManifestNodeReferences must be strings")
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

        return self.unique_id.split(".")[0]

    @property
    def node(self) -> ManifestNode:
        """
        The manifest node this reference points to.
        """

        return self.manifest_artifact.resources[self.unique_id]


class ManifestSourceNode(ArtifactNodeReader, Model):
    """Details about a Source node."""

    _test_path = "manifest.sources['source.poffertjes_shop.raw.products']"

    fqn: List[str]
    """ The fqn attribute """

    database: Optional[str]
    """ The database attribute """

    db_schema: str
    """ The db_schema attribute """

    unique_id: str
    """ The unique_id attribute """

    package_name: str
    """ The package_name attribute """

    root_path: str
    """ The root_path attribute """

    path: str
    """ The path attribute """

    original_file_path: str
    """ The original_file_path attribute """

    name: str
    """ The name attribute """

    source_name: str
    """ The source_name attribute """

    source_description: str
    """ The source_description attribute """

    loader: str
    """ The loader attribute """

    identifier: str
    """ The identifier attribute """

    resource_type: str
    """ The resource_type attribute """

    quoting: Optional[Quoting]
    """ The quoting attribute """

    loaded_at_field: Optional[str]
    """ The loaded_at_field attribute """

    freshness: Optional[FreshnessThreshold]
    """ The freshness attribute """

    external: Optional[ExternalTable]
    """ The external attribute """

    description: Optional[str]
    """ The description attribute """

    columns: Optional[Dict[str, ColumnInfo]]
    """ The columns attribute """

    meta: Optional[Dict]
    """ The meta attribute """

    source_meta: Optional[Dict]
    """ The source_meta attribute """

    tags: Optional[List[str]]
    """ The tags attribute """

    config: Optional[SourceConfig]
    """ The config attribute """

    patch_path: Optional["str"]
    """ The patch_path attribute """

    unrendered_config: Optional[Dict]
    """ The unrendered_config attribute """

    relation_name: Optional["str"]
    """ The relation_name attribute """

    created_at: Optional[float]
    """ The created_at attribute """

    class Config:
        fields = {
            "db_schema": "schema",
        }


class MacroArgument(Model):
    """Details about the arguments of a macro"""

    _test_path = (
        'manifest.macros["macro.poffertjes_shop.convert_currency"].arguments[0]'
    )

    name: str
    """ The name attribute """

    type: Optional["str"]
    """ The type attribute """

    description: Optional["str"]
    """ The description attribute """


class ManifestMacroNode(ArtifactNodeReader, Model):
    """Details about a Macro node."""

    _test_path = (
        'manifest.macros["macro.poffertjes_shop.create_or_replace_table_raw_orders"]'
    )

    unique_id: str
    """ The unique_id attribute """

    package_name: str
    """ The package_name attribute """

    root_path: str
    """ The root_path attribute """

    path: str
    """ The path attribute """

    original_file_path: str
    """ The original_file_path attribute """

    name: str
    """ The name attribute """

    macro_sql: str
    """ The macro_sql attribute """

    resource_type: str
    """ The resource_type attribute """

    tags: Optional[List[str]]
    """ The tags attribute """

    patch_path: Optional[str]
    """ The patch_path attribute """

    created_at: Optional[float]
    """ The created_at attribute """

    description: Optional[str]
    """ The description attribute """

    meta: Optional[dict]
    """ The meta attribute """

    docs: Optional[dict]
    """ The docs attribute """

    arguments: Optional[List[MacroArgument]]
    """ The arguments attribute """

    depends_on: Optional[Dict[str, List[str]]]
    """ The depends_on attribute """


class ManifestDocsNode(Model):
    """Details about a Docs node."""

    _test_path = 'manifest.docs["dbt.__overview__"]'

    unique_id: str
    """ The unique_id attribute """

    package_name: str
    """ The package_name attribute """

    root_path: str
    """ The root_path attribute """

    path: str
    """ The path attribute """

    original_filepath: Optional["str"]
    """ The original_filepath attribute """

    name: str
    """ The name attribute """

    block_contents: str
    """ The block_contents attribute """


class ManifestExposureNode(ArtifactNodeReader, Model):
    """Details about an Exposure node."""

    _test_path = 'manifest.exposures["exposure.poffertjes_shop.revenue_summary"]'

    fqn: List[str]
    """ The fqn attribute """

    unique_id: str
    """ The unique_id attribute """

    package_name: str
    """ The package_name attribute """

    root_path: str
    """ The root_path attribute """

    path: str
    """ The path attribute """

    original_file_path: str
    """ The original_file_path attribute """

    name: str
    """ The name attribute """

    node_type: str
    """ The node_type attribute """

    owner: dict
    """ The owner attribute """

    resource_type: Optional["str"]
    """ The resource_type attribute """

    description: Optional["str"]
    """ The description attribute """

    maturity: Optional["str"]
    """ The maturity attribute """

    meta: Optional[Dict]
    """ The meta attribute """

    tags: Optional[List[str]]
    """ The tags attribute """

    url: Optional["str"]
    """ The url attribute """

    refs: Optional[List[list]]
    """ The refs attribute """

    sources: Optional[List[list]]
    """ The sources attribute """

    created_at: Optional[float]
    """ The created_at attribute """

    depends_on: Optional[Dict[str, list]]
    """ The depends_on attribute """

    class Config:
        fields = {"db_schema": "schema", "node_type": "type"}


class MetricFilter(Model):
    """Details about a Metric filter."""

    _test_path = "manifest.metrics['metric.poffertjes_shop.revenue'].filters[0]"

    field: str
    """ The field attribute """

    operator: str
    """ The operator attribute """

    value: str
    """ The value attribute """


class ManifestMetricNode(ArtifactNodeReader, Model):
    """Details about a Metric node."""

    _test_path = "manifest.metrics['metric.poffertjes_shop.revenue']"

    fqn: List[str]
    """ The fqn attribute """

    unique_id: str
    """ The unique_id attribute """

    package_name: str
    """ The package_name attribute """

    root_path: str
    """ The root_path attribute """

    path: str
    """ The path attribute """

    original_file_path: str
    """ The original_file_path attribute """

    model: str
    """ The model attribute """

    name: str
    """ The name attribute """

    description: str
    """ The description attribute """

    label: str
    """ The label attribute """

    node_type: str
    """ The node_type attribute """

    filters: List[MetricFilter]
    """ The filters attribute """

    time_grains: List[str]
    """ The time_grains attribute """

    dimensions: List[str]
    """ The dimensions attribute """

    sql: Optional["str"]
    """ The sql attribute """

    timestamp: Optional["str"]
    """ The timestamp attribute """

    resource_type: Optional["str"]
    """ The resource_type attribute """

    meta: Optional[Dict]
    """ The meta attribute """

    tags: Optional[list]
    """ The tags attribute """

    sources: Optional[List[str]]
    """ The sources attribute """

    refs: Optional[List[List[str]]]
    """ The refs attribute """

    created_at: Optional[float]
    """ The created_at attribute """

    depends_on: Optional[Dict]
    """ The depends_on attribute """

    class Config:
        fields = {"node_type": "type"}


class CatalogNode(ArtifactNodeReader, Model):
    """Details about a Catalog node."""

    _test_path = 'catalog.nodes["model.poffertjes_shop.customers"]'

    metadata: "CatalogNodeMetadata"
    """ The metadata attribute """

    columns: Dict[str, "CatalogNodeColumn"]
    """ The columns attribute """

    stats: Dict[str, "CatalogNodeStats"]
    """ The stats attribute """

    unique_id: str
    """ The unique_id attribute """


class CatalogNodeMetadata(Model):
    """Metadata details about a CatalogNode."""

    _test_path = 'catalog.nodes["model.poffertjes_shop.customers"].metadata'

    node_type: str
    """ The node_type attribute """

    db_schema: str
    """ The db_schema attribute """

    name: str
    """ The name attribute """

    database: Optional["str"]
    """ The database attribute """

    comment: Optional["str"]
    """ The comment attribute """

    owner: Optional["str"]
    """ The owner attribute """

    class Config:
        fields = {"db_schema": "schema", "node_type": "type"}


class CatalogNodeColumn(Model):
    """Details about the columns in a CatalogNode."""

    _test_path = (
        'catalog.nodes["model.poffertjes_shop.customers"].columns["customer_id"]'
    )

    node_type: str
    """ The node_type attribute """

    index: int
    """ The index attribute """

    name: str
    """ The name attribute """

    comment: Optional["str"]
    """ The comment attribute """

    class Config:
        fields = {"node_type": "type"}


class CatalogNodeStats(Model):
    """Statics about a CatalogNode."""

    _test_path = 'catalog.nodes["model.poffertjes_shop.customers"].stats["has_stats"]'

    description: Optional["str"]
    """ The description attribute """

    id: str
    """ The id attribute """

    include: bool
    """ The include attribute """

    label: str
    """ The label attribute """

    value: Optional["str"]
    """ The value attribute """


RunResultsModel.update_forward_refs()
ManifestModel.update_forward_refs()
CatalogModel.update_forward_refs()
SourcesModel.update_forward_refs()
CatalogNode.update_forward_refs()

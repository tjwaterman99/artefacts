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

    class Config:
        fields = {
            "db_schema": "schema",
        }

    raw_sql: str
    compiled: Optional["str"]
    database: Optional["str"]
    db_schema: str
    fqn: List[str]
    unique_id: str
    package_name: str
    root_path: str
    path: str
    original_file_path: str
    name: str
    resource_type: Literal["snapshot"]
    alias: str
    checksum: dict
    config: Optional[Dict]
    tags: Optional[List[str]]
    refs: Optional[List]
    sources: Optional[List[List[str]]]
    depends_on: Optional[Dict]
    description: Optional[str]
    columns: Optional[Dict]
    meta: Optional[Dict]
    docs: Optional[Dict]
    patch_path: Optional[str]
    compiled_path: Optional[str]
    build_path: Optional[str]
    deferred: Optional[bool]
    unrendered_config: Optional[dict]
    created_at: Optional[float]
    config_call_dict: Optional[dict]
    compiled_sql: Optional[str]
    extra_ctes_injected: Optional[bool]
    extra_ctes: Optional[List[Dict]]
    relation_name: Optional[str]

    _test_path = "manifest.nodes['snapshot.poffertjes_shop.orders_snapshot']"


class ManifestSeedNode(ArtifactNodeReader, Model):
    """
    An object representing a seed in the dbt project.

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

    class Config:
        fields = {
            "db_schema": "schema",
        }

    raw_sql: str
    compiled: Optional["str"]
    database: Optional["str"]
    db_schema: str
    fqn: List[str]
    unique_id: str
    package_name: str
    root_path: str
    path: str
    original_file_path: str
    name: str
    resource_type: Literal["seed"]
    alias: str
    checksum: dict
    config: Optional[Dict]
    tags: Optional[List[str]]
    refs: Optional[List]
    sources: Optional[List[List[str]]]
    depends_on: Optional[Dict]
    description: Optional[str]
    columns: Optional[Dict]
    meta: Optional[Dict]
    docs: Optional[Dict]
    patch_path: Optional[str]
    compiled_path: Optional[str]
    build_path: Optional[str]
    deferred: Optional[bool]
    unrendered_config: Optional[dict]
    created_at: Optional[float]
    config_call_dict: Optional[dict]
    compiled_sql: Optional[str]
    extra_ctes_injected: Optional[bool]
    extra_ctes: Optional[List[Dict]]
    relation_name: Optional[str]

    _test_path = "manifest.nodes['seed.poffertjes_shop.shoppes']"


ManifestModelUnion = Union[
    ManifestModelNode,
    ManifestTestNode,
    ManifestOperationNode,
    ManifestSnapshotNode,
    ManifestSeedNode,
]

ManifestNode = Annotated[
    ManifestModelUnion, pydantic.Field(discriminator="resource_type")
]


class ManifestModel(Model):
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

    metadata: "Metadata"
    nodes: Dict[str, ManifestNode]
    sources: Dict[str, "ManifestSourceNode"]
    macros: Dict[str, "ManifestMacroNode"]
    docs: Dict[str, "ManifestDocsNode"]
    exposures: Dict[str, "ManifestExposureNode"]
    metrics: Dict[str, "ManifestMetricNode"]
    selectors: dict
    disabled: Optional[Dict]
    parent_map: Optional[Dict[str, List["ManifestNodeReference"]]]
    child_map: Optional[Dict[str, List["ManifestNodeReference"]]]

    @property
    def resources(self) -> Dict:
        """A dictionary containing all resources defined in the dbt project"""

        return {
            **self.nodes,
            **self.sources,
            **self.macros,
            **self.exposures,
            **self.metrics,
        }

    def iter_resource_type(
        self, resource_type: str, package_name: str = None
    ) -> Iterable:
        """Iterate over all resources of a specific type

        Args:
            resource_type (str): The type of resource, eg 'model', 'source',
                                 'exposure', etc.
            package_name (str): nly return resources from the specified dbt package.
        """

        for k, v in self.resources.items():
            if package_name and v.package_name != package_name:
                continue
            if v.resource_type == resource_type:
                yield v


class RunResultsModel(Model):
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

    _test_path = "run_results"

    metadata: "Metadata"
    results: List["RunResultNode"]
    elapsed_time: float
    args: Optional[Dict]


class CatalogModel(Model):
    """The catalog artifact.

    Attributes:
        metadata: The metadata attribute of the catalog
        nodes: The nodes attribute of the catalog
        sources: The sources attribute of the catalog
        errors: The errors attribute of the catalog

    """

    _test_path = "catalog"

    metadata: "Metadata"
    nodes: Dict[str, "CatalogNode"]
    sources: Dict[str, "CatalogNode"]
    errors: Optional[List[str]]


class SourcesModel(Model):
    """The sources artifact.

    Attributes:
        metadata: The metadata attribute
        results: The results attribute
        elapsed_time: The elapsed_time attribute

    """

    _test_path = "sources"

    metadata: "Metadata"
    results: List["SourcesFreshnessResult"]
    elapsed_time: float


class Metadata(Model):
    """Data about the context in which the artifact was generated.

    Attributes:
        generated_at: The generated_at attribute
        invocation_id: The invocation_id attribute
        env: The env attribute
        project_id: The project_id attribute
        user_id: The user_id attribute
        send_anonymous_usage_stats: The send_anonymous_usage_stats attribute
        adapter_type: The adapter_type attribute
        dbt_schema_version_raw: The raw string containing information about the dbt schema version
        dbt_version_raw: The raw string containing information about the dbt-core version

    """

    _test_path = "manifest.metadata"

    dbt_schema_version_raw: str
    dbt_version_raw: str
    generated_at: datetime.datetime
    invocation_id: uuid.UUID
    env: dict
    project_id: Optional["str"]
    user_id: Optional["str"]
    send_anonymous_usage_stats: Optional[bool]
    adapter_type: Optional["str"]

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
    identifier: Optional[bool]
    db_schema: Optional[bool]
    column: Optional[bool]

    class Config:
        fields = {
            "db_schema": "schema",
        }


class ExternalPartition(Model):
    """
    Object representing a partition on an external table

    Attributes:
        name: The name attribute
        description: The description attribute
        data_type: The data_type attribute
        meta: The meta attribute

    """

    _test_path = (
        "manifest.sources['source.poffertjes_shop.raw.external_events']"
        ".external.partitions[0]"
    )

    name: Optional["str"]
    description: Optional["str"]
    data_type: Optional["str"]
    meta: Optional[Dict]


class ExternalTable(Model):
    """
    Object representing an external table

    Attributes:
        location: The location attribute
        file_format: The file_format attribute
        row_format: The row_format attribute
        tbl_properties: The tbl_properties attribute
        partitions: The partitions attribute

    """

    _test_path = (
        "manifest.sources['source.poffertjes_shop.raw.external_events'].external"
    )

    location: Optional[str]
    file_format: Optional[str]
    row_format: Optional[str]
    tbl_properties: Optional[str]
    partitions: Optional[List[ExternalPartition]]


class ColumnInfo(Model):
    """Column details of a documented model

    Attributes:
        name: The name attribute
        description: The description attribute
        meta: The meta attribute
        data_type: The data_type attribute
        quote: The quote attribute
        tags: The tags attribute

    """

    _test_path = (
        "manifest.sources['source.poffertjes_shop.raw.orders'].columns['order_id']"
    )

    name: str
    description: Optional[str]
    meta: Optional[dict]
    data_type: Optional[str]
    quote: Optional[bool]
    tags: Optional[List[str]]


class TimingResult(Model):
    """Timing details from running the node.

    Attributes:
        name: the name attribute
        started_at: the started_at attribute
        completed_at: the completed_at attribute

    """

    _test_path = "sources.results[0].timing[0]"

    name: str
    started_at: Optional[datetime.datetime]
    completed_at: Optional[datetime.datetime]


class SourceConfig(Model):
    """An object containing details about a source's config

    Attributes:
        enabled: Whether the source is enabled
    """

    _test_path = "manifest.sources['source.poffertjes_shop.raw.products'].config"

    enabled: Optional[bool]


class Time(Model):
    """An object representing a time interval, used for example when
    configuring a source freshness check

    Attributes:
        period: The length of the time interval, eg days, hours, seconds
        count: The number of periods associed with the time interval
    """

    _test_path = (
        "manifest.sources['source.poffertjes_shop.raw.products'].freshness.error_after"
    )

    count: Optional[int]
    period: Optional["str"]


class FreshnessThreshold(Model):
    """Details of the criteria used when checking a source's freshness

    Attributes:
        warn_after: The freshness criteria after which a freshness check will
                    raise a warning.
        error_after: The freshness criteria after which a freshness check will
                     raise an error.
        filter: A SQL statement used to filter the table when running a
                freshness check.
    """

    _test_path = "manifest.sources['source.poffertjes_shop.raw.products'].freshness"

    warn_after: Optional[Time]
    error_after: Optional[Time]
    filter: Optional["str"]


class SourcesFreshnessResult(ArtifactNodeReader, Model):
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

    _test_path = "sources.results[0]"

    unique_id: str
    status: str
    error: Optional[str]
    max_loaded_at: Optional[str]
    snapshotted_at: Optional[str]
    max_loaded_at_time_ago_in_s: Optional[float]
    criteria: Optional[FreshnessThreshold]
    adapter_response: Optional[dict]
    timing: Optional[List[TimingResult]]
    thread_id: Optional[str]
    execution_time: Optional[float]


class RunResultNode(ArtifactNodeReader, Model):
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

    _test_path = "run_results.results[0]"

    status: str
    timing: List[TimingResult]
    thread_id: str
    execution_time: float
    adapter_response: dict
    message: Optional["str"]
    failures: Optional[int]
    unique_id: str


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

    _test_path = "manifest.sources['source.poffertjes_shop.raw.products']"

    fqn: List[str]
    database: Optional[str]
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
    quoting: Optional[Quoting]
    loaded_at_field: Optional[str]
    freshness: Optional[FreshnessThreshold]
    external: Optional[ExternalTable]
    description: Optional[str]
    columns: Optional[Dict[str, ColumnInfo]]
    meta: Optional[Dict]
    source_meta: Optional[Dict]
    tags: Optional[List[str]]
    config: Optional[SourceConfig]
    patch_path: Optional["str"]
    unrendered_config: Optional[Dict]
    relation_name: Optional["str"]
    created_at: Optional[float]

    class Config:
        fields = {
            "db_schema": "schema",
        }


class MacroArgument(Model):
    """Details about the arguments of a macro

    Attributes:
        name: The name attribute
        type: The type attribute
        description: The description attribute

    """

    _test_path = (
        'manifest.macros["macro.poffertjes_shop.convert_currency"].arguments[0]'
    )

    name: str
    type: Optional["str"]
    description: Optional["str"]


class ManifestMacroNode(ArtifactNodeReader, Model):
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

    _test_path = (
        'manifest.macros["macro.poffertjes_shop.create_or_replace_table_raw_orders"]'
    )

    unique_id: str
    package_name: str
    root_path: str
    path: str
    original_file_path: str
    name: str
    macro_sql: str
    resource_type: str
    tags: Optional[List[str]]
    patch_path: Optional[str]
    created_at: Optional[float]
    description: Optional[str]
    meta: Optional[dict]
    docs: Optional[dict]
    arguments: Optional[List[MacroArgument]]
    depends_on: Optional[Dict[str, List[str]]]


class ManifestDocsNode(Model):
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

    _test_path = 'manifest.docs["dbt.__overview__"]'

    unique_id: str
    package_name: str
    root_path: str
    path: str
    original_filepath: Optional["str"]
    name: str
    block_contents: str


class ManifestExposureNode(ArtifactNodeReader, Model):
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

    _test_path = 'manifest.exposures["exposure.poffertjes_shop.revenue_summary"]'

    fqn: List[str]
    unique_id: str
    package_name: str
    root_path: str
    path: str
    original_file_path: str
    name: str
    node_type: str
    owner: dict
    resource_type: Optional["str"]
    description: Optional["str"]
    maturity: Optional["str"]
    meta: Optional[Dict]
    tags: Optional[List[str]]
    url: Optional["str"]
    refs: Optional[List[list]]
    sources: Optional[List[list]]
    created_at: Optional[float]
    depends_on: Optional[Dict[str, list]]

    class Config:
        fields = {"db_schema": "schema", "node_type": "type"}


class MetricFilter(Model):
    """Details about a Metric filter.

    Attributes:
        field: The field attribute
        operator: The operator attribute
        value: The value attribute
    """

    _test_path = "manifest.metrics['metric.poffertjes_shop.revenue'].filters[0]"

    field: str
    operator: str
    value: str


class ManifestMetricNode(ArtifactNodeReader, Model):
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

    _test_path = "manifest.metrics['metric.poffertjes_shop.revenue']"

    fqn: List[str]
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
    filters: List[MetricFilter]
    time_grains: List[str]
    dimensions: List[str]
    sql: Optional["str"]
    timestamp: Optional["str"]
    resource_type: Optional["str"]
    meta: Optional[Dict]
    tags: Optional[list]
    sources: Optional[List[str]]
    refs: Optional[List[List[str]]]
    created_at: Optional[float]
    depends_on: Optional[Dict]

    class Config:
        fields = {"node_type": "type"}


class CatalogNode(ArtifactNodeReader, Model):
    """Details about a Catalog node.

    Attributes:
        metadata: The metadata attribute
        columns: The columns attribute
        stats: The stats attribute
        unique_id: The unique_id attribute

    """

    _test_path = 'catalog.nodes["model.poffertjes_shop.customers"]'

    metadata: "CatalogNodeMetadata"
    columns: Dict[str, "CatalogNodeColumn"]
    stats: Dict[str, "CatalogNodeStats"]
    unique_id: str


class CatalogNodeMetadata(Model):
    """Metadata details about a CatalogNode.

    Attributes:
        node_type: The node_type attribute
        db_schema: The db_schema attribute
        name: The name attribute
        database: The database attribute
        comment: The comment attribute
        owner: The owner attribute

    """

    _test_path = 'catalog.nodes["model.poffertjes_shop.customers"].metadata'

    node_type: str
    db_schema: str
    name: str
    database: Optional["str"]
    comment: Optional["str"]
    owner: Optional["str"]

    class Config:
        fields = {"db_schema": "schema", "node_type": "type"}


class CatalogNodeColumn(Model):
    """Details about the columns in a CatalogNode.

    Attributes:
        node_type: The node_type attribute
        index: The index attribute
        name: The name attribute
        comment: The comment attribute

    """

    _test_path = (
        'catalog.nodes["model.poffertjes_shop.customers"].columns["customer_id"]'
    )

    node_type: str
    index: int
    name: str
    comment: Optional["str"]

    class Config:
        fields = {"node_type": "type"}


class CatalogNodeStats(Model):
    """Statics about a CatalogNode.

    Attributes:
        description: The description of the statistic
        id: The id of the statistic
        include: TODO
        label: The label of the statistic
        value: The value of the statistic
    """

    _test_path = 'catalog.nodes["model.poffertjes_shop.customers"].stats["has_stats"]'

    description: Optional["str"]
    id: str
    include: bool
    label: str
    value: Optional["str"]


RunResultsModel.update_forward_refs()
ManifestModel.update_forward_refs()
CatalogModel.update_forward_refs()
SourcesModel.update_forward_refs()
CatalogNode.update_forward_refs()

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
ManifestNode = typing.ForwardRef('ManifestNode')
RunResultNode = typing.ForwardRef('RunResultNode')


class Artifact:

    @classmethod
    def path(cls):
        return os.path.join(conf.dbt_target_dir, cls.name() + '.json')

    @classmethod
    def name(cls):
        return re.sub(r'(?<!^)(?=[A-Z])', '_', cls.__name__).lower()

    @classmethod
    def load(cls):
        if not artefacts.state.exists(cls.name()):
            with open(cls.path(), 'r') as artifact_fh:
                raw_artifact = json.load(artifact_fh)
            artefacts.state.set(cls.name(), cls.parse_obj(raw_artifact))              
        return artefacts.state.get(cls.name())  


class ArtifactReader:

    @property
    def run_results_artifact(self):
        return self.get_artifact('run_results')

    @property
    def manifest_artifact(self):
        return self.get_artifact('manifest')

    @property
    def catalog_artifact(self):
        return self.get_artifact('catalog')

    @property
    def sources_artifact(self):
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


class Manifest(Artifact, pydantic.BaseModel):
    metadata: Metadata
    nodes: typing.Dict[str, ManifestNode]
    sources: dict
    macros: dict
    docs: dict
    exposures: dict
    metrics: dict
    selectors: dict
    disabled: typing.Union[dict, None]
    parent_map: typing.Union[dict, None]
    child_map: typing.Union[dict, None]


class RunResults(Artifact, pydantic.BaseModel):
    metadata: Metadata
    results: typing.List[RunResultNode]
    elapsed_time: float
    args: typing.Union[dict, None]


class Catalog(Artifact, pydantic.BaseModel):
    metadata: Metadata
    nodes: typing.Dict[str, dict]
    sources: typing.Dict[str, dict]
    errors: typing.Union[typing.List[str], None]


class Sources(Artifact, pydantic.BaseModel):
    metadata: Metadata
    results: typing.List[dict]
    elapsed_time: float


class Metadata(pydantic.BaseModel):
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


class RunResultNode(ArtifactReader, pydantic.BaseModel):
    status: str
    timing: typing.List[dict]
    thread_id: str
    execution_time: float
    adapter_response: dict
    message: typing.Union[str, None]
    failures: typing.Union[int, None]
    unique_id: str

    @property
    def manifest(self):
        return self.manifest_artifact.nodes.get(self.unique_id)


class ManifestNode(ArtifactReader, pydantic.BaseModel):
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


RunResults.update_forward_refs()
Manifest.update_forward_refs()
Catalog.update_forward_refs()
Sources.update_forward_refs()

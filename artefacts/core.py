import os
import json
import re
import pydantic
import typing

import artefacts.state
from artefacts.config import conf


Metadata = typing.ForwardRef('Metadata')


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


# TODO: mixin with convenience methods for accessing the `state` of an
# artifact and error notifications if that artifact is not compiled
class ArtifactReader():
    pass


class Manifest(Artifact, pydantic.BaseModel):
    metadata: Metadata


class RunResults(Artifact, pydantic.BaseModel):
    metadata: Metadata


class Catalog(Artifact, pydantic.BaseModel):
    metadata: Metadata


class Sources(Artifact, pydantic.BaseModel):
    metadata: Metadata


class Metadata(pydantic.BaseModel):
    dbt_schema_version: str
    dbt_version: str
    generated_at: str


RunResults.update_forward_refs()
Manifest.update_forward_refs()
Catalog.update_forward_refs()
Sources.update_forward_refs()

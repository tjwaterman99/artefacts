import os
import json
import re
import pydantic
from typing import ForwardRef

import artefacts.state
import artefacts.config


Metadata = ForwardRef('Metadata')


class Artifact:
    
    @classmethod
    def load(cls):
        return artefacts.state.get_or_set(cls.name, cls._setup())

    @classmethod
    def name(cls):
        return re.sub(r'(?<!^)(?=[A-Z])', '_', cls.__name__).lower()

    @classmethod
    def _setup(cls):
        conf = artefacts.state.get_or_set('config', artefacts.config.Config())
        artifact_path = os.path.join(conf.dbt_target_dir, cls.name() + '.json')

        with open(artifact_path, 'r') as artifact_fh:
            raw_artifact = json.load(artifact_fh)
        
        return artefacts.state.set(cls.name(), cls.parse_obj(raw_artifact))    


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


class Metadata(pydantic.BaseModel):
    dbt_schema_version: str


RunResults.update_forward_refs()
Manifest.update_forward_refs()
Catalog.update_forward_refs()

import json
import pydantic

import artefacts.state
import artefacts.config


# TODO: abstract base model with loading functionality
class Artifact():
    pass


# TODO: mixin with convenience methods for accessing the `state` of an
# artifact and error notifications if that artifact is not compiled
class ArtifactReader():
    pass


class Manifest(pydantic.BaseModel):

    metadata: dict

    @classmethod
    def load(cls):
        return artefacts.state.get_or_set('manifest', cls._setup())

    @classmethod
    def _setup(cls):
        conf = artefacts.state.get_or_set('config', artefacts.config.Config())
        
        with open(conf.manifest_path, 'r') as manifest_fh:
            raw_manifest = json.load(manifest_fh)
        
        return artefacts.state.set('manifest', cls.parse_obj(raw_manifest))


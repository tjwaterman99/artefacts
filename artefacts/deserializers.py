import abc

from .models import ManifestModel, RunResultsModel, SourcesModel, CatalogModel
from .loaders import FileSystemLoader
from .config import Config

import artefacts.state


class ArtifactDeserializer(abc.ABC):

    @abc.abstractproperty
    def name(self):
        pass

    @abc.abstractproperty
    def model(self):
        pass

    def __new__(cls, Loader=FileSystemLoader, **config_kwargs):
        if artefacts.state.exists(cls.name):
            return artefacts.state.get(cls.name)
        else:
            artifact = cls.deserialize(Loader=Loader, **config_kwargs)
            return artefacts.state.set(cls.name, artifact)

    @classmethod
    def deserialize(cls, Loader=FileSystemLoader, **config_kwargs):
        config = Config(**config_kwargs)
        loader = Loader(config=config)
        raw_artifact = loader.load(cls.name)
        parsed_artifact = cls.model.parse_obj(raw_artifact)
        return parsed_artifact


class Manifest(ArtifactDeserializer):
    name = 'manifest'
    model = ManifestModel


class RunResults(ArtifactDeserializer):
    name = 'run_results'
    model = RunResultsModel


class Sources(ArtifactDeserializer):
    name = 'sources'
    model = SourcesModel


class Catalog(ArtifactDeserializer):
    name = 'catalog'
    model = CatalogModel


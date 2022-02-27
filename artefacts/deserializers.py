import abc
from typing import ClassVar

from .models import ManifestModel, RunResultsModel, SourcesModel, CatalogModel
from .loaders import FileSystemLoader
from .config import Config

import artefacts.state


class ArtifactDeserializer(abc.ABC):
    @abc.abstractproperty
    def artifact_name(self) -> str:
        pass

    @abc.abstractproperty
    def model(self):
        pass

    def __new__(cls, Loader=FileSystemLoader, config=None):
        if artefacts.state.exists(cls.artifact_name):
            return artefacts.state.get(cls.artifact_name)
        else:
            artifact = cls.deserialize(Loader=Loader, config=config)
            return artefacts.state.set(cls.artifact_name, artifact)

    @classmethod
    def get_or_set_config(cls, config=None):
        if artefacts.state.exists("config"):
            return artefacts.state.get("config")
        elif config is None:
            config = Config()
            return artefacts.state.set("config", config)
        else:
            return artefacts.state.set("config", config)

    @classmethod
    def deserialize(cls, Loader=FileSystemLoader, config=None):
        config = cls.get_or_set_config(config=config)
        loader = Loader(config=config)
        raw_artifact = loader.load(cls.artifact_name)
        parsed_artifact = cls.model.parse_obj(raw_artifact)
        return parsed_artifact


class Manifest(ManifestModel, ArtifactDeserializer):
    artifact_name: ClassVar = "manifest"
    model = ManifestModel


class RunResults(RunResultsModel, ArtifactDeserializer):
    artifact_name: ClassVar = "run_results"
    model = RunResultsModel


class Sources(SourcesModel, ArtifactDeserializer):
    artifact_name: ClassVar = "sources"
    model = SourcesModel


class Catalog(CatalogModel, ArtifactDeserializer):
    artifact_name: ClassVar = "catalog"
    model = CatalogModel

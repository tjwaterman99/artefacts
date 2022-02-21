from typing import Dict
from collections.abc import Mapping
import abc
import toml
import os


class ConfigReader(Mapping):
    def __init__(self, extras: Dict = dict()):
        _data = self.load()
        _data.update(extras)
        self.data = self.parse(_data)

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        for k, v in self.data.items():
            yield k

    def __len__(self):
        return len(self.data)

    def items(self):
        for k in self:
            yield k, self[k]

    @abc.abstractmethod
    def parse(self, data: Dict = dict()) -> Dict:
        pass

    @abc.abstractmethod
    def load(self) -> Dict:
        pass


class EnvConfig(ConfigReader):
    def load(self, environ: Dict = os.environ) -> Dict:
        return dict(environ)

    def parse(self, data) -> Dict:
        extracted = {k: v for k, v in data.items() if k.startswith("ARTEFACTS_")}
        parsed = {k.replace("ARTEFACTS_", "").lower(): v for k, v in extracted.items()}
        return parsed


class PyProjectConfig(ConfigReader):
    def load(self):
        return {}

    def parse(self, data):
        return data


class KeywordConfig(ConfigReader):
    def __init__(self, **kwargs):
        self.data = {**kwargs}

    def parse(self):
        pass

    def load(self):
        pass


class NewConfig(Mapping):
    def __init__(self, **kwargs):
        self.keyword_config = KeywordConfig(**kwargs)
        self.pyproject_config = PyProjectConfig()
        self.env_config = EnvConfig()
        self.conf = {
            **self.pyproject_config,
            **self.env_config,
            **self.keyword_config
        }

    def __getitem__(self, item):
        return self.conf[item]

    def __len__(self):
        return len(self.conf)

    def __iter__(self):
        return iter(self.conf)


class Config:
    """
    artefacts configuration object.
    """

    def __init__(
        self,
        config_filename="pyproject.toml",
        config_abspath=os.path.abspath(os.getcwd()),
    ):
        self.config_filename = config_filename
        self.config_abspath = config_abspath
        self.config_filepath = os.path.join(config_abspath, config_filename)
        try:
            self.raw = toml.load(self.config_filepath)
        except FileNotFoundError:
            self.raw = dict()

        if "artefacts" not in self.raw:
            self.raw["artefacts"] = dict()

        self._dbt_project_dir = (
            self.raw["artefacts"].get("dbt_project_dir")
            or os.environ.get("DBT_PROJECT_DIR")
            or "."
        )
        self._dbt_target_dir = (
            self.raw["artefacts"].get("dbt_target_dir")
            or os.environ.get("DBT_TARGET_DIR")
            or "target"
        )

    @property
    def dbt_target_dir(self):
        return os.path.abspath(
            os.path.join(self._dbt_project_dir, self._dbt_target_dir)
        )

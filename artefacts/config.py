from collections.abc import Mapping
import toml
import os


class Config(Mapping):
    defaults = {
        "dbt_project_dir": ".",
        "dbt_target_dir": "target",
    }

    def __init__(self, **kwargs):
        self.pyproject_path = kwargs.get("pyproject_path", ".")
        self.pyproject_filename = kwargs.get("pyproject_filename", "pyproject.toml")
        self.env_config = self.load_env_config()
        self.pyproject_config = self.load_pyproject_config(
            pyproject_path=self.pyproject_path,
            pyproject_filename=self.pyproject_filename,
        )
        self.data = {
            **self.defaults,
            **self.pyproject_config,
            **self.env_config,
            **kwargs,
        }

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        for k, v in self.data.items():
            yield k

    def __len__(self):
        return len(self.data)

    def load_env_config(self):
        extracted = {k: v for k, v in os.environ.items() if k.startswith("ARTEFACTS_")}
        parsed = {k.replace("ARTEFACTS_", "").lower(): v for k, v in extracted.items()}
        return parsed

    def load_pyproject_config(self, pyproject_path, pyproject_filename):
        filename = os.path.join(pyproject_path, pyproject_filename)
        try:
            pyproject = toml.load(filename)
            return pyproject.get("artefacts", dict())
        except FileNotFoundError:
            return dict()

    @property
    def dbt_target_dir(self):
        return os.path.abspath(
            os.path.join(self["dbt_project_dir"], self["dbt_target_dir"])
        )

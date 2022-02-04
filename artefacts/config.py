import toml
import os


class Config:
    """
    artefacts configuration object.
    """

    config_filename = 'pyproject.toml'
    config_abspath = os.path.abspath(os.getcwd())
    config_filepath = os.path.join(config_abspath, config_filename)

    def __init__(self):
        try:
            self.raw = toml.load(self.config_filepath)
        except FileNotFoundError:
            self.raw = dict()

        if 'artefacts' not in self.raw:
            self.raw['artefacts'] = dict()

        self._dbt_project_dir = self.raw['artefacts'].get('dbt_project_dir') or os.environ.get('DBT_PROJECT_DIR') or '.'
        self._dbt_target_dir = self.raw['artefacts'].get('dbt_target_dir') or os.environ.get('DBT_TARGET_DIR') or 'target'

    @property
    def dbt_target_dir(self):
        return os.path.abspath(os.path.join(self._dbt_project_dir, self._dbt_target_dir))


conf = Config()

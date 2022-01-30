import toml
import os

import artefacts.state


class Config:
    """
    artefacts configuration object.
    """

    config_filename = 'pyproject.toml'
    config_abspath = os.path.abspath(os.getcwd())
    config_filepath = os.path.join(config_abspath, config_filename)

    def __init__(self):
        self.raw = toml.load(self.config_filepath)

        if 'artefacts' not in self.raw:
            self.raw['artefacts'] = dict()

        self._dbt_project_dir = self.raw['artefacts'].get('dbt_project_dir') or os.environ.get('DBT_PROJECT_DIR') or '.'
        self._dbt_target_dir = self.raw['artefacts'].get('dbt_target_dir') or os.environ.get('DBT_TARGET_DIR') or 'target'

        artefacts.state.set('config', self)

    @property
    def dbt_target_dir(self):
        return os.path.abspath(os.path.join(self._dbt_project_dir, self._dbt_target_dir))

    @property
    def manifest_path(self):
        return os.path.join(self.dbt_target_dir, 'manifest.json')

    @property
    def run_results_path(self):
        return os.path.join(self.dbt_target_dir, 'run_results.json')

    @property
    def catalog_path(self):
        return os.path.join(self.dbt_target_dir, 'catalog.json')

    @property
    def sources_path(self):
        return os.path.join(self.dbt_target_dir, 'sources.json')

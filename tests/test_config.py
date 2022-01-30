import os

from artefacts.config import Config
import artefacts.state


def test_config_target_path():
    conf = Config()
    assert os.environ['DBT_PROJECT_DIR'] in conf.dbt_target_dir
    assert conf.dbt_target_dir.endswith('target')


def test_config_sets_state():
    conf = Config()
    assert artefacts.state.get('config') == conf

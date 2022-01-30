import os

from artefacts.config import Config


def test_config_target_path():
    conf = Config()
    assert os.environ['DBT_PROJECT_DIR'] in conf.dbt_target_dir
    assert conf.dbt_target_dir.endswith('target')
    

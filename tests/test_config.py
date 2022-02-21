import os

from artefacts.config import Config, EnvConfig, KeywordConfig, NewConfig


def test_config_target_path():
    conf = Config()
    assert os.environ["DBT_PROJECT_DIR"] in conf.dbt_target_dir
    assert conf.dbt_target_dir.endswith("target")


def test_env_config():
    conf = EnvConfig(extras={"ARTEFACTS_TEST": 1})
    assert conf["test"] == 1


def test_keyword_config():
    conf = KeywordConfig(test=1)
    assert conf["test"] == 1


def test_config():
    conf = NewConfig(x=1)
    assert conf["x"] == 1

    os.environ["ARTEFACTS_TEST"] = "1"
    conf = NewConfig()
    assert conf["test"] == "1"

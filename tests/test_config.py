import pytest
import os

from artefacts.config import Config
from .conftest import testing_poffertjes_shop  # noqa


@pytest.mark.skipif("not testing_poffertjes_shop")
def test_config_target_path(config):
    assert config["dbt_project_dir"] == "dbt_projects/poffertjes_shop"
    assert config["dbt_target_dir"] == "target"
    assert os.environ["ARTEFACTS_DBT_PROJECT_DIR"] in config.dbt_target_dir
    assert config.dbt_target_dir.endswith("target")


def test_config_priority_order():
    os.environ["ARTEFACTS_TEST"] = "1"
    assert Config()["test"] == "1"
    assert Config(test=2)["test"] == 2
    assert Config().env_config["test"] == "1"


def test_config_length(config):
    assert len(config) > 0


def test_config_iter(config):
    assert list(iter(config)) != []


def test_config_load_project_config(config):
    assert config.load_pyproject_config(".", "pyproject.toml")["testing"] == 1
    assert config["testing"] == 1

    resp = config.load_pyproject_config(".", "dne")
    assert resp == dict()

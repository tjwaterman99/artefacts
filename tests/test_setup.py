# Validate that the project has been set up correctly.

import os
import pytest


@pytest.fixture
def dbt_project_dir():
    return os.environ['DBT_PROJECT_DIR']


def test_dbt_project_exists(dbt_project_dir):
    assert len(os.listdir(dbt_project_dir)) > 0


def test_dbt_project_is_built(dbt_project_dir):
    target_dir = os.path.join(dbt_project_dir, 'target')
    assert os.path.exists(target_dir)
    assert 'manifest.json' in os.listdir(target_dir)
    assert 'run_results.json' in os.listdir(target_dir)

# Validate that the project and fixtures have been set up correctly.

import os

import artefacts.state


def test_dbt_project_exists(dbt_project_dir):
    assert len(os.listdir(dbt_project_dir)) > 0


def test_dbt_project_is_built(dbt_project_dir):
    target_dir = os.path.join(dbt_project_dir, "target")
    assert os.path.exists(target_dir)
    assert "manifest.json" in os.listdir(target_dir)
    assert "run_results.json" in os.listdir(target_dir)


def test_clean_state_is_clean(clean_state):
    assert artefacts.state._state == dict()
    assert not artefacts.state.exists("manifest")


def test_default_state_has_artefacts(manifest):
    assert artefacts.state.get("manifest") == manifest

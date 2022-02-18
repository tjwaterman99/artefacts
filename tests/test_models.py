import pytest

import artefacts.state
from artefacts.deserializers import (
    Manifest, 
    Catalog, 
    Sources,
    RunResults
)
from artefacts.models import (
    ManifestModel,
    ArtifactReader,
    RunResultNode, 
    ManifestNode, 
    RunResultsModel
)


def test_manifest_validates_dbt_version(manifest):
    assert ManifestModel.validate_metadata(manifest.metadata)

    # Quick way to check that some validation is being ran.
    outdated_metadata = manifest.metadata.copy(deep=True)
    outdated_metadata.dbt_version_raw = '0.21'
    assert outdated_metadata.dbt_version.major == 0

    with pytest.raises(ValueError):
        ManifestModel.validate_metadata(outdated_metadata)


def test_metadata_dbt_schema_version(all_artifacts):
    assert all_artifacts.metadata.dbt_schema_version > 0


def test_metadata_dbt_version(all_artifacts):
    assert all_artifacts.metadata.dbt_version.major > 0


def test_run_result_nodes_have_manifest(manifest, run_results):
    for result in run_results.results:
        assert result.manifest == manifest.nodes.get(result.unique_id)


def test_manifest_parent_map(manifest):
    for k, v in manifest.parent_map.items():
        for node_reference in v:
            assert node_reference.node is not None
            assert node_reference.resource_type == node_reference.node.resource_type


def test_manifest_child_map(manifest):
    for k, v in manifest.child_map.items():
        for node_reference in v:
            assert node_reference.node is not None
            assert node_reference.resource_type == node_reference.node.resource_type


def test_run_results_loads():
    run_results = RunResults()
    assert artefacts.state.run_results == run_results


def test_sources_loads():
    sources = Sources()
    assert artefacts.state.sources == sources

import pytest

from .conftest import testing_poffertjes_shop
from artefacts.mixins import ArtifactNodeReader


def test_node_readers_have_manifest(manifest):
    for k, v in manifest.resources.items():
        assert v.manifest.unique_id == v.unique_id


@pytest.mark.skipif("not testing_poffertjes_shop")
def test_models_have_catalog(manifest):
    for model in manifest.iter_resource_type('model'):
        assert model.catalog.unique_id == model.unique_id


@pytest.mark.skipif("not testing_poffertjes_shop")
def test_models_have_run_results(manifest):
    for model in manifest.iter_resource_type('model'):
        assert model.run_results[0].unique_id == model.unique_id


@pytest.mark.skipif("not testing_poffertjes_shop")
def test_source_have_freshness_checks(manifest):
    for source in manifest.iter_resource_type('source'):
        assert source.freshness_check_results[0].unique_id == source.unique_id


@pytest.mark.skipif("not testing_poffertjes_shop")
def test_models_have_parents(manifest):
    for model in manifest.iter_resource_type('model'):
        assert len(model.parents) > 0


@pytest.mark.skipif("not testing_poffertjes_shop")
def test_sources_have_children(manifest):
    source = manifest.resources['source.poffertjes_shop.raw.orders']
    assert len(source.children) > 0


@pytest.mark.skipif("not testing_poffertjes_shop")
def test_sources_have_snapshots(manifest):
    source = manifest.resources['source.poffertjes_shop.raw.orders']
    assert len(source.snapshots) > 0


@pytest.mark.skipif("not testing_poffertjes_shop")
def test_models_have_tests(manifest):
    model = manifest.resources['model.poffertjes_shop.base_orders']
    assert len(model.tests) > 0

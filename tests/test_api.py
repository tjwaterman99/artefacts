import pytest

from artefacts.api import (
    models,
    tests as _tests,
    seeds,
    sources,
    docs,
    macros,
    exposures,
    metrics,
    selectors,
    operations,
    snapshots,
)
from .conftest import testing_poffertjes_shop  # noqa


@pytest.mark.skipif("not testing_poffertjes_shop")
def test_operations():
    assert len(operations()) > 0
    assert len(operations(package_name="dbt_utils")) == 0
    assert len(operations(package_name="poffertjes_shop")) > 0


@pytest.mark.skipif("not testing_poffertjes_shop")
def test_snapshots():
    assert len(snapshots()) > 0
    assert len(snapshots(package_name="dbt_utils")) == 0
    assert len(snapshots(package_name="poffertjes_shop")) > 0


@pytest.mark.skipif("not testing_poffertjes_shop")
def test_models():
    assert len(models()) > 0
    assert len(models(package_name="dbt_utils")) == 0
    assert len(models(package_name="poffertjes_shop")) > 0


@pytest.mark.skipif("not testing_poffertjes_shop")
def test_tests():
    assert len(_tests()) > 0
    assert len(_tests(package_name="dbt_utils")) == 0
    assert len(_tests(package_name="poffertjes_shop")) > 0


@pytest.mark.skipif("not testing_poffertjes_shop")
def test_macros():
    assert len(macros()) > 0
    assert len(macros(package_name="dbt_utils")) > 0
    assert len(macros(package_name="poffertjes_shop")) > 0


@pytest.mark.skipif("not testing_poffertjes_shop")
def test_seeds():
    assert len(seeds()) > 0
    assert len(seeds(package_name="dbt_utils")) == 0
    assert len(seeds(package_name="poffertjes_shop")) > 0


@pytest.mark.skipif("not testing_poffertjes_shop")
def test_sources():
    assert len(sources()) > 0
    assert len(sources(package_name="dbt_utils")) == 0
    assert len(sources(package_name="poffertjes_shop")) > 0


@pytest.mark.skipif("not testing_poffertjes_shop")
def test_exposures():
    assert len(exposures()) > 0
    assert len(exposures(package_name="dbt_utils")) == 0
    assert len(exposures(package_name="poffertjes_shop")) > 0


@pytest.mark.skipif("not testing_poffertjes_shop")
def test_metrics():
    assert len(metrics()) > 0
    assert len(metrics(package_name="dbt_utils")) == 0
    assert len(metrics(package_name="poffertjes_shop")) > 0


@pytest.mark.skipif("not testing_poffertjes_shop")
def test_docs():
    assert len(docs()) > 0


@pytest.mark.skipif("not testing_poffertjes_shop")
def test_selectors():
    assert len(selectors()) > 0

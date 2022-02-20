import os
import pytest

from artefacts.api import models
from artefacts.api import tests as _tests
from artefacts.api import seeds
from artefacts.api import sources
from artefacts.api import docs
from artefacts.api import macros
from artefacts.api import exposures
from artefacts.api import metrics
from artefacts.api import selectors
from artefacts.api import operations
from artefacts.api import snapshots


dbt_project = os.environ["DBT_PROJECT_DIR"].split("/")[-1]


@pytest.mark.skipif("dbt_project != 'poffertjes_shop'")
def test_operations():
    assert len(operations()) > 0
    assert len(operations(package_name="dbt_utils")) == 0
    assert len(operations(package_name="poffertjes_shop")) > 0


@pytest.mark.skipif("dbt_project != 'poffertjes_shop'")
def test_snapshots():
    assert len(snapshots()) > 0
    assert len(snapshots(package_name="dbt_utils")) == 0
    assert len(snapshots(package_name="poffertjes_shop")) > 0


@pytest.mark.skipif("dbt_project != 'poffertjes_shop'")
def test_models():
    assert len(models()) > 0
    assert len(models(package_name="dbt_utils")) == 0
    assert len(models(package_name="poffertjes_shop")) > 0


@pytest.mark.skipif("dbt_project != 'poffertjes_shop'")
def test_tests():
    assert len(_tests()) > 0
    assert len(_tests(package_name="dbt_utils")) == 0
    assert len(_tests(package_name="poffertjes_shop")) > 0


@pytest.mark.skipif("dbt_project != 'poffertjes_shop'")
def test_macros():
    assert len(macros()) > 0
    assert len(macros(package_name="dbt_utils")) > 0
    assert len(macros(package_name="poffertjes_shop")) > 0


@pytest.mark.skipif("dbt_project != 'poffertjes_shop'")
def test_seeds():
    assert len(seeds()) > 0
    assert len(seeds(package_name="dbt_utils")) == 0
    assert len(seeds(package_name="poffertjes_shop")) > 0


@pytest.mark.skipif("dbt_project != 'poffertjes_shop'")
def test_sources():
    assert len(sources()) > 0
    assert len(sources(package_name="dbt_utils")) == 0
    assert len(sources(package_name="poffertjes_shop")) > 0


@pytest.mark.skipif("dbt_project != 'poffertjes_shop'")
def test_exposures():
    assert len(exposures()) > 0
    assert len(exposures(package_name="dbt_utils")) == 0
    assert len(exposures(package_name="poffertjes_shop")) > 0


@pytest.mark.skipif("dbt_project != 'poffertjes_shop'")
def test_metrics():
    assert len(metrics()) > 0
    assert len(metrics(package_name="dbt_utils")) == 0
    assert len(metrics(package_name="poffertjes_shop")) > 0


@pytest.mark.skipif("dbt_project != 'poffertjes_shop'")
def test_docs():
    assert len(docs()) > 0


@pytest.mark.skipif("dbt_project != 'poffertjes_shop'")
def test_selectors():
    assert len(selectors()) > 0

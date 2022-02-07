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


dbt_project = os.environ['DBT_PROJECT_DIR'].split('/')[-1]


@pytest.mark.skipif("dbt_project != 'poffertjes_shop'")
def test_models():
    assert len(models()) > 0


@pytest.mark.skipif("dbt_project != 'poffertjes_shop'")
def test_tests():
    assert len(_tests()) > 0


@pytest.mark.skipif("dbt_project != 'poffertjes_shop'")
def test_seeds():
    assert len(seeds()) > 0


@pytest.mark.skipif("dbt_project != 'poffertjes_shop'")
def test_sources():
    assert len(sources()) > 0


@pytest.mark.skipif("dbt_project != 'poffertjes_shop'")
def test_exposures():
    assert len(exposures()) > 0


@pytest.mark.skipif("dbt_project != 'poffertjes_shop'")
def test_metrics():
    assert len(metrics()) > 0


@pytest.mark.skipif("dbt_project != 'poffertjes_shop'")
def test_docs():
    assert len(docs()) > 0


@pytest.mark.skipif("dbt_project != 'poffertjes_shop'")
def test_selectors():
    assert len(selectors()) > 0

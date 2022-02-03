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


def test_models():
    assert len(models()) > 0


def test_tests():
    assert len(_tests()) > 0


def test_seeds():
    assert len(seeds()) > 0


def test_sources():
    assert len(sources()) > 0


@pytest.mark.skip
def test_exposures():
    assert len(exposures()) > 0


@pytest.mark.skip
def test_metrics():
    assert len(metrics()) > 0


def test_docs():
    assert len(docs()) > 0


@pytest.mark.skip
def test_selectors():
    assert len(selectors()) > 0

from artefacts.api import models
from artefacts.api import tests as _tests


def test_models():
    assert len(models()) > 0


def test_tests():
    assert len(_tests()) > 0

import pytest


@pytest.fixture(autouse=True, scope='session')
def add_artefacts(doctest_namespace):
    import artefacts
    doctest_namespace["artefacts"] = artefacts

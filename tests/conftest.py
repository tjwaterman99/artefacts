import pytest

from artefacts import Manifest, RunResults, Catalog, Sources


@pytest.fixture(scope='session', params=[Manifest, RunResults, Catalog, Sources])
def all_artifacts(request):
    yield request.param.load()


@pytest.fixture(scope='session')
def manifest():
    return Manifest.load()


@pytest.fixture(scope='session')
def catalog():
    return Catalog.load()


@pytest.fixture(scope='session')
def run_results():
    return RunResults.load()


@pytest.fixture(scope='session')
def sources():
    return Sources.load()

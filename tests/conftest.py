import pytest

from artefacts import Manifest, RunResults, Catalog, Sources


@pytest.fixture(scope='module', params=[Manifest, RunResults, Catalog, Sources])
def all_artifacts(request):
    yield request.param.load()

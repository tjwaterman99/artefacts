import pytest

from artefacts.deserializers import Manifest, RunResults, Catalog, Sources
import artefacts


@pytest.fixture
def dbt_project_dir():
    return os.environ['DBT_PROJECT_DIR']


@pytest.fixture(scope='session', params=[Manifest, RunResults, Catalog, Sources])
def all_artifacts(request):
    yield request.param()


@pytest.fixture(scope='session')
def manifest():
    return Manifest()


@pytest.fixture(scope='session')
def catalog():
    return Catalog()


@pytest.fixture(scope='session')
def run_results():
    return RunResults()


@pytest.fixture(scope='session')
def sources():
    return Sources()

import os
import pytest

from artefacts.deserializers import Manifest, RunResults, Catalog, Sources
import artefacts


testing_poffertjes_shop = os.environ['DBT_PROJECT_DIR'] == "dbt_projects/poffertjes_shop"


def iter_base_models():
    import artefacts.models
    for name in dir(artefacts.models):
        obj = getattr(artefacts.models, name)
        try:
            if (
                issubclass(obj, artefacts.models.Deserializer) \
                and obj != artefacts.models.Deserializer
            ):
                yield obj
        except TypeError:  # Raised when `obj` is not a class
            pass


@pytest.fixture(scope='session')
def reference_docs():
    with open('docs/reference.rst', 'r') as fh:
        return fh.read()


@pytest.fixture(scope='session', params=list(iter_base_models()))
def base_model(request):
    yield request.param


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

import os
import pytest

from artefacts.deserializers import Manifest, RunResults, Catalog, Sources
from artefacts.config import Config
import artefacts.state


testing_poffertjes_shop = (
    os.environ["ARTEFACTS_DBT_PROJECT_DIR"] == "dbt_projects/poffertjes_shop"
)


# I think this should be named something like `deserializer_classes` because
# the term "base model" already has a meaning in dbt projects
def iter_base_models():
    import artefacts.models

    for name in dir(artefacts.models):
        obj = getattr(artefacts.models, name)
        try:
            if (
                issubclass(obj, artefacts.models.Model)
                and obj != artefacts.models.Model
            ):
                yield obj
        except TypeError:  # Raised when `obj` is not a class
            pass


def iter_node_reader_classes():
    import artefacts.mixins

    for klass in iter_base_models():
        if issubclass(klass, artefacts.mixins.ArtifactNodeReader):
            yield klass


@pytest.fixture(scope="function")
def config():
    return Config()


@pytest.fixture(scope="function")
def clean_state(monkeypatch):
    monkeypatch.setattr(artefacts.state, "_state", dict())


@pytest.fixture(scope="session")
def reference_docs():
    with open("docs/reference.rst", "r") as fh:
        return fh.read()


@pytest.fixture(scope="session")
def compiled_reference_docs():
    with open('docs/_build/reference.html') as fh:
        return fh.read()


@pytest.fixture(scope="session", params=list(iter_node_reader_classes()))
def node_reader_class(request):
    yield request.param


@pytest.fixture(scope="session", params=list(iter_base_models()))
def base_model(request):
    yield request.param


@pytest.fixture
def dbt_project_dir():
    return os.environ["ARTEFACTS_DBT_PROJECT_DIR"]


@pytest.fixture(scope="session", params=[Manifest, RunResults, Catalog, Sources])
def all_artifacts(request):
    yield request.param()


@pytest.fixture(scope="session")
def manifest():
    return Manifest()


@pytest.fixture(scope="session")
def catalog():
    return Catalog()


@pytest.fixture(scope="session")
def run_results():
    return RunResults()


@pytest.fixture(scope="session")
def sources():
    return Sources()

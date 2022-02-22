from artefacts.deserializers import Manifest, Catalog, RunResults, Sources
from artefacts.config import Config
import artefacts.state


def test_manifest_deserialize():
    manifest = Manifest.deserialize()
    assert type(manifest) == Manifest.model


def test_catalog_deserialize():
    catalog = Catalog.deserialize()
    assert type(catalog) == Catalog.model


def test_run_results_deserialize():
    run_results = RunResults.deserialize()
    assert type(run_results) == RunResults.model


def test_sources_deserialize():
    sources = Sources.deserialize()
    assert type(sources) == Sources.model


def test_catalog_sets_state(clean_state):
    assert artefacts.state.get("catalog") is None
    catalog = Catalog()
    assert artefacts.state.get("catalog") == catalog


def test_manifest_sets_state(clean_state):
    assert artefacts.state.get("manifest") is None
    manifest = Manifest()
    assert artefacts.state.get("manifest") == manifest


def test_run_results_sets_state(clean_state):
    assert artefacts.state.get("manifest") is None
    run_results = RunResults()
    assert artefacts.state.get("run_results") == run_results


def test_sources_sets_state(clean_state):
    assert artefacts.state.get("manifest") is None
    sources = Sources()
    assert artefacts.state.get("sources") == sources


def test_loading_deserializer_caches_config(clean_state):
    assert artefacts.state.get('config') is None
    manifest = Manifest()
    assert artefacts.state.get('config') == Config()


def test_loading_deserializer_uses_cached_config(clean_state):
    config = Config(random=200)
    manifest = Manifest(config=config)
    assert Manifest.get_or_set_config() == config
    run_results = RunResults()
    assert RunResults.get_or_set_config() == config

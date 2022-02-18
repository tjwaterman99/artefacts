from artefacts.deserializers import Manifest, Catalog, RunResults, Sources


def test_manifest_deserialize():
    manifest = Manifest.deserialize()
    assert type(manifest) == Manifest.model


def test_catalog_deserialize():
    catalog = Catalog.deserialize()
    assert type(catalog) == Catalog.model


def test_run_results_deserialize():
    run_results = RunResults.deserialize()
    assert type(run_results) == RunResults.model


def test_manifest_deserialize():
    sources = Sources.deserialize()
    assert type(sources) == Sources.model
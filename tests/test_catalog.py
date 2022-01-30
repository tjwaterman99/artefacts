from artefacts import Catalog
import artefacts.state


def test_catalog_loads():
    catalog = Catalog.load()
    assert artefacts.state.catalog == catalog

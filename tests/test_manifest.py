from artefacts import Manifest
import artefacts.state


def test_manifest_loads():
    manifest = Manifest.load()
    assert artefacts.state.manifest == manifest

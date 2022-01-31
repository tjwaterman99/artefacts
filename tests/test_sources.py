from artefacts import Sources
import artefacts.state


def test_sources_loads():
    sources = Sources.load()
    assert artefacts.state.sources == sources

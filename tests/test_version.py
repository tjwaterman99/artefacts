import toml
import artefacts


def test_version():
    project = toml.load('pyproject.toml')
    assert project['tool']['poetry']['version'] == artefacts.__version__

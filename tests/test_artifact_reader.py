import pytest

from artefacts.core import ArtifactReader


@pytest.mark.parametrize("artifact_name", ['manifest', 'run_results', 'catalog', 'sources'])
def test_artifact_reader_loads(artifact_name):
    reader = ArtifactReader()
    assert reader.get_artifact(artifact_name).name() == artifact_name


@pytest.mark.parametrize("artifact_name", ['manifest', 'run_results', 'catalog', 'sources'])
def test_artifact_reader_has_artifact_attribute(artifact_name):
    reader = ArtifactReader()
    assert getattr(reader, f"{artifact_name}_artifact").name() == artifact_name

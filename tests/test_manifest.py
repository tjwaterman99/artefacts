import pytest

from artefacts import Manifest
import artefacts.state


def test_manifest_loads():
    manifest = Manifest.load()
    assert artefacts.state.manifest == manifest


def test_manifest_validates_dbt_version(manifest):
    assert Manifest.validate_metadata(manifest.metadata)

    # Quick way to check that some validation is being ran.
    outdated_metadata = manifest.metadata.copy(deep=True)
    outdated_metadata.dbt_version_raw = '0.21'
    assert outdated_metadata.dbt_version.major == 0

    with pytest.raises(ValueError):
        Manifest.validate_metadata(outdated_metadata)

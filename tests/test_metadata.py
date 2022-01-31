

def test_metadata_dbt_schema_version(all_artifacts):
    assert all_artifacts.metadata.dbt_schema_version > 0


def test_metdata_dbt_version(all_artifacts):
    assert all_artifacts.metadata.dbt_version.major > 0

import pytest
from pydantic import BaseModel

from .conftest import testing_poffertjes_shop  # noqa

from artefacts.models import ManifestModel


def test_manifest_resources(manifest):
    assert len(manifest.resources) > 0
    assert type(manifest.resources) == dict


@pytest.mark.skipif("not testing_poffertjes_shop")
@pytest.mark.parametrize("resource_type", ["model", "test", "source", "metric"])
def test_manifest_iter_resource_type(resource_type, manifest):
    assert len(list(manifest.iter_resource_type(resource_type))) > 0
    for resource in manifest.iter_resource_type(resource_type):
        assert resource.resource_type == resource_type


@pytest.mark.skipif("not testing_poffertjes_shop")
def test_manifest_iter_resource_with_package_name(manifest):
    package_names = ["poffertjes_shop", "dbt_utils"]
    for pn in package_names:
        for resource in manifest.iter_resource_type("model", package_name=pn):
            assert resource.package_name == pn


def test_models_have_reference_defined(base_model, reference_docs):
    assert base_model._qualpath() in reference_docs


@pytest.mark.skipif("not testing_poffertjes_shop")
def test_models_are_deserialized_at_least_once(
    manifest, sources, run_results, catalog, base_model
):
    if not hasattr(base_model, "_test_path"):
        pytest.skip()
    else:
        context = {
            "manifest": manifest,
            "catalog": catalog,
            "run_results": run_results,
            "sources": sources,
            "base_model": base_model,
        }
        exec(f"example = {base_model._test_path}", context)
        assert type(context["example"]) == base_model


def test_models_have_docs_path(base_model):
    assert base_model._qualpath() in base_model._docs_path()


def test_models_raise_attribute_error_with_docs_path(base_model):
    with pytest.raises(AttributeError) as err:
        base_model.some_attribute_that_does_not_exist
        assert base_model._docs_path() in str(err)


def test_manifest_validates_dbt_version(manifest):
    assert ManifestModel.validate_metadata(manifest.metadata)

    # Quick way to check that some validation is being ran.
    outdated_metadata = manifest.metadata.copy(deep=True)
    outdated_metadata.dbt_version_raw = "0.21"
    assert outdated_metadata.dbt_version.major == 0

    with pytest.raises(ValueError):
        ManifestModel.validate_metadata(outdated_metadata)


def test_metadata_dbt_schema_version(all_artifacts):
    assert all_artifacts.metadata.dbt_schema_version > 0


def test_metadata_dbt_version(all_artifacts):
    assert all_artifacts.metadata.dbt_version.major > 0


def test_run_result_nodes_have_manifest(manifest, run_results):
    for result in run_results.results:
        assert result.manifest == manifest.nodes.get(result.unique_id)


def test_manifest_parent_map(manifest):
    for k, v in manifest.parent_map.items():
        for node_reference in v:
            assert node_reference.node is not None
            assert node_reference.resource_type == node_reference.node.resource_type


def test_manifest_child_map(manifest):
    for k, v in manifest.child_map.items():
        for node_reference in v:
            assert node_reference.node is not None
            assert node_reference.resource_type == node_reference.node.resource_type


def test_models_have_attribute_docs(base_model, compiled_reference_docs):
    errors = []
    allowed_exceptions = ["get_artifact", "validate_metadata"]
    attributes = [
        a for a in dir(base_model) if a not in dir(BaseModel) and not a.startswith("_")
    ] + list(base_model.__annotations__.keys())

    attribute_docs_path = [
        base_model._docs_path().split("#")[-1] + "." + a for a in attributes
    ]

    for docpath, attribute in zip(attribute_docs_path, attributes):
        if (
            docpath not in compiled_reference_docs
            and attribute not in allowed_exceptions
        ):
            errors.append(attribute)

    if any(errors):
        msg = f"Missing attribute docs for {str(base_model)} attributes: {errors}"
        raise Exception(msg)

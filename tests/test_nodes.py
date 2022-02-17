from artefacts.core import RunResultNode, ManifestNode


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

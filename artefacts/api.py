"""
API
===

The artefacts API contains helper methods for interacting with dbt's artifacts.
"""

import typing

from artefacts.core import Manifest, ManifestNode


def models() -> typing.List[ManifestNode]:
    """
    A list of all models in the dbt project.
    """

    result = []
    manifest = Manifest.load()
    for k,v in manifest.nodes.items():
        if v.resource_type == 'model':
            result.append(v)
    else:
        return result


def tests() -> typing.List[ManifestNode]:
    """
    A list of all tests in the dbt project
    """

    result = []
    manifest = Manifest.load()
    for k,v in manifest.nodes.items():
        if v.resource_type == 'test':
            result.append(v)
    else:
        return result

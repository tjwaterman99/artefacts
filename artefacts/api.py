"""
The artefacts API contains helper methods for interacting with dbt's artifacts.
"""

import typing

from artefacts.core import (
    Manifest, ManifestNode, ManifestSourceNode, ManifestDocsNode,
    ManifestExposureNode, ManifestMacroNode, ManifestMetricNode
)


def models() -> typing.List[ManifestNode]:
    """ A list of all models in the dbt project. """

    result = []
    manifest = Manifest.load()
    for k,v in manifest.nodes.items():
        if v.resource_type == 'model':
            result.append(v)
    else:
        return result


def tests() -> typing.List[ManifestNode]:
    """ A list of all tests in the dbt project. """

    result = []
    manifest = Manifest.load()
    for k,v in manifest.nodes.items():
        if v.resource_type == 'test':
            result.append(v)
    else:
        return result


def seeds() -> typing.List[ManifestNode]:
    """A list of all seeds in the dbt project. """

    result = []
    manifest = Manifest.load()
    for k,v in manifest.nodes.items():
        if v.resource_type == 'seed':
            result.append(v)
    else:
        return result


def sources() -> typing.List[ManifestSourceNode]:
    """A list of all sources in the dbt project. """

    manifest = Manifest.load()
    return list(manifest.sources.values())


def docs() -> typing.List[ManifestDocsNode]:
    """A list of all documentation nodes in the dbt project. """

    manifest = Manifest.load()
    return list(manifest.docs.values())


def docs() -> typing.List[ManifestMacroNode]:
    """A list of all macros in the dbt project. """

    manifest = Manifest.load()
    return list(manifest.macros.values())


def exposures() -> typing.List[ManifestExposureNode]:
    """A list of all exposures defined in the dbt project. """

    manifest = Manifest.load()
    return list(manifest.exposures.values())


def metrics() -> typing.List[ManifestMetricNode]:
    """A list of all metrics in the dbt project. """

    manifest = Manifest.load()
    return list(manifest.metrics.values())


def selectors() -> dict:
    """A list of all selectors defined in the dbt project. """

    manifest = Manifest.load()
    return list(manifest.selectors.values())


"""
The artefacts API contains helper methods for interacting with dbt's artifacts.
"""

import typing

from artefacts.deserializers import Manifest
from artefacts.models import (
    ManifestNode,
    ManifestSourceNode,
    ManifestDocsNode,
    ManifestExposureNode,
    ManifestMacroNode,
    ManifestMetricNode,
)


def models(package_name: str = None) -> typing.List[ManifestNode]:
    """A list of all models in the dbt project.

    Args:
        package_name (str): Only return models from the specified dbt package.
                            Defaults to returning models from all packages.

    >>> model = artefacts.api.models()[0]
    >>> model.resource_type
    'model'
    >>> type(model)
    <class 'artefacts.models.ManifestNode'>

    """

    manifest = Manifest()
    return list(manifest.iter_resource_type("model", package_name=package_name))


def tests(package_name: str = None) -> typing.List[ManifestNode]:
    """A list of all tests in the dbt project.

    Args:
        package_name (str): Only return tests from the specified dbt package.
                            Defaults to returning tests from all packages.

    >>> test = artefacts.api.tests()[0]
    >>> test.resource_type
    'test'
    >>> type(test)
    <class 'artefacts.models.ManifestNode'>

    """

    manifest = Manifest()
    return list(manifest.iter_resource_type("test", package_name=package_name))


def seeds(package_name: str = None) -> typing.List[ManifestNode]:
    """A list of all seeds in the dbt project.

    Args:
        package_name (str): Only return seeds from the specified dbt package.
                            Defaults to returning seeds from all packages.

    >>> seed = artefacts.api.seeds()[0]
    >>> seed.resource_type
    'seed'
    >>> type(seed)
    <class 'artefacts.models.ManifestNode'>

    """

    manifest = Manifest()
    return list(manifest.iter_resource_type("seed", package_name=package_name))


def snapshots(package_name: str = None) -> typing.List[ManifestNode]:
    """A list of all snapshots in the dbt project.

    Args:
        package_name (str): Only return snapshots from the specified dbt package.
                            Defaults to returning snapshots from all packages.

    >>> snapshot = artefacts.api.snapshots()[0]
    >>> snapshot.resource_type
    'snapshot'
    >>> type(snapshot)
    <class 'artefacts.models.ManifestNode'>

    """

    manifest = Manifest()
    return list(manifest.iter_resource_type("snapshot", package_name=package_name))


def operations(package_name: str = None) -> typing.List[ManifestNode]:
    """A list of all operations in the dbt project.

    Args:
        package_name (str): Only return operations from the specified dbt package.
                            Defaults to returning operations from all packages.

    >>> operation = artefacts.api.operations()[0]
    >>> operation.resource_type
    'operation'
    >>> type(operation)
    <class 'artefacts.models.ManifestNode'>

    """

    manifest = Manifest()
    return list(manifest.iter_resource_type("operation", package_name=package_name))


def sources(package_name: str = None) -> typing.List[ManifestSourceNode]:
    """A list of all sources in the dbt project.

    Args:
        package_name (str): Only return sources from the specified dbt package.
                            Defaults to returning sources from all packages.

    >>> source = artefacts.api.sources()[0]
    >>> source.resource_type
    'source'
    >>> type(source)
    <class 'artefacts.models.ManifestSourceNode'>

    """

    manifest = Manifest()
    return list(manifest.iter_resource_type("source", package_name=package_name))


def docs() -> typing.List[ManifestDocsNode]:
    """A list of all documentation nodes in the dbt project.

    >>> doc = artefacts.api.docs()[0]
    >>> type(doc)
    <class 'artefacts.models.ManifestDocsNode'>

    """

    manifest = Manifest()
    return list(manifest.docs.values())


def macros(package_name: str = None) -> typing.List[ManifestMacroNode]:
    """A list of all macros in the dbt project.

    Args:
        package_name (str): Only return macros from the specified dbt package.
                            Defaults to returning macros from all packages.

    >>> macro = artefacts.api.macros()[0]
    >>> macro.resource_type
    'macro'
    >>> type(macro)
    <class 'artefacts.models.ManifestMacroNode'>

    """

    manifest = Manifest()
    return list(manifest.iter_resource_type("macro", package_name=package_name))


def exposures(package_name: str = None) -> typing.List[ManifestExposureNode]:
    """A list of all exposures defined in the dbt project.

    Args:
        package_name (str): Only return exposures from the specified dbt package.
                            Defaults to returning exposures from all packages.

    >>> exposure = artefacts.api.exposures()[0]
    >>> exposure.resource_type
    'exposure'
    >>> type(exposure)
    <class 'artefacts.models.ManifestExposureNode'>

    """

    manifest = Manifest()
    return list(manifest.iter_resource_type("exposure", package_name=package_name))


def metrics(package_name: str = None) -> typing.List[ManifestMetricNode]:
    """A list of all metrics in the dbt project.

    Args:
        package_name (str): Only return metrics from the specified dbt package.
                            Defaults to returning metrics from all packages.

    >>> metric = artefacts.api.metrics()[0]
    >>> metric.resource_type
    'metric'
    >>> type(metric)
    <class 'artefacts.models.ManifestMetricNode'>

    """

    manifest = Manifest()
    return list(manifest.iter_resource_type("metric", package_name=package_name))


def selectors() -> typing.List[dict]:
    """A list of all selectors defined in the dbt project.

    >>> selector = artefacts.api.selectors()[0]
    >>> type(selector)
    <class 'dict'>

    """

    manifest = Manifest()
    return list(manifest.selectors.values())

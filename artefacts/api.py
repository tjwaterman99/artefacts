"""
The artefacts API contains helper methods for interacting with dbt's artifacts.
"""

import typing

from artefacts.core import (
    Manifest, ManifestNode, ManifestSourceNode, ManifestDocsNode,
    ManifestExposureNode, ManifestMacroNode, ManifestMetricNode
)


def models() -> typing.List[ManifestNode]:
    """ A list of all models in the dbt project. 
    
    >>> model = artefacts.api.models()[0]
    >>> model.resource_type
    'model'
    >>> type(model)
    <class 'artefacts.core.ManifestNode'>

    """

    result = []
    manifest = Manifest.load()
    for k,v in manifest.nodes.items():
        if v.resource_type == 'model':
            result.append(v)
    else:
        return result


def tests() -> typing.List[ManifestNode]:
    """ A list of all tests in the dbt project. 

    >>> test = artefacts.api.tests()[0]
    >>> test.resource_type
    'test'
    >>> type(test)
    <class 'artefacts.core.ManifestNode'>
    
    """

    result = []
    manifest = Manifest.load()
    for k,v in manifest.nodes.items():
        if v.resource_type == 'test':
            result.append(v)
    else:
        return result


def seeds() -> typing.List[ManifestNode]:
    """A list of all seeds in the dbt project. 

    >>> seed = artefacts.api.seeds()[0]
    >>> seed.resource_type
    'seed'
    >>> type(seed)
    <class 'artefacts.core.ManifestNode'>
    
    """

    result = []
    manifest = Manifest.load()
    for k,v in manifest.nodes.items():
        if v.resource_type == 'seed':
            result.append(v)
    else:
        return result


def sources() -> typing.List[ManifestSourceNode]:
    """A list of all sources in the dbt project. 
    
    >>> source = artefacts.api.sources()[0]
    >>> source.resource_type
    'source'
    >>> type(source)
    <class 'artefacts.core.ManifestSourceNode'>

    """

    manifest = Manifest.load()
    return list(manifest.sources.values())


def docs() -> typing.List[ManifestDocsNode]:
    """A list of all documentation nodes in the dbt project. 

    >>> doc = artefacts.api.docs()[0]
    >>> type(doc)
    <class 'artefacts.core.ManifestDocsNode'>
    
    """

    manifest = Manifest.load()
    return list(manifest.docs.values())


def macros() -> typing.List[ManifestMacroNode]:
    """A list of all macros in the dbt project. 
    
    >>> macro = artefacts.api.macros()[0]
    >>> macro.resource_type
    'macro'
    >>> type(macro)
    <class 'artefacts.core.ManifestMacroNode'>
    
    """

    manifest = Manifest.load()
    return list(manifest.macros.values())


def exposures() -> typing.List[ManifestExposureNode]:
    """A list of all exposures defined in the dbt project. 

    >>> exposure = artefacts.api.exposures()[0]
    >>> exposure.resource_type
    'exposure'
    >>> type(exposure)
    <class 'artefacts.core.ManifestExposureNode'>
    
    """

    manifest = Manifest.load()
    return list(manifest.exposures.values())


def metrics() -> typing.List[ManifestMetricNode]:
    """A list of all metrics in the dbt project. 
    
    >>> metric = artefacts.api.metrics()[0]
    >>> metric.resource_type
    'metric'
    >>> type(metric)
    <class 'artefacts.core.ManifestMetricNode'>
    
    """

    manifest = Manifest.load()
    return list(manifest.metrics.values())


def selectors() -> typing.List[dict]:
    """A list of all selectors defined in the dbt project. 

    >>> selector = artefacts.api.selectors()[0]
    >>> type(selector)
    <class 'dict'>
    
    """

    manifest = Manifest.load()
    return list(manifest.selectors.values())


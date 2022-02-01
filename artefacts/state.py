"""
artefacts.state
===============

A simple key-value store for holding the parsed artifacts. Using this store
enables us to avoid loading or parsing the artifacts multiple times. To use
the store, simply import the module directly.

>>> import artefacts.state

"""

import typing


def set(key: str, value: typing.Any) -> typing.Union[typing.Any, None]:
    """
    Places an object in the store.

    >>> artefacts.state.set('myitem', {'a': 1})
    {'a': 1}

    """
    
    globals()[key] = value
    return globals()[key]


def get(key: str) -> typing.Union[typing.Any, None]:
    """
    Returns an object from the store, if it exists.

    >>> artefacts.state.get('myitem')
    {a: 1}

    """

    return globals().get(key)


def exists(key: str) -> bool:
    """
    Returns `True` if the key exists in the store.

    >>> artefacts.state.exists('myitem')
    True
    >>> artefacts.state.exists('thisdoesnotexist')
    False

    """
    return key in globals()


def get_or_set(key, value):
    return get(key) or set(key, value)

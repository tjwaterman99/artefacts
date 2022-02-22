"""
artefacts.state
===============

A simple key-value store for holding the parsed artifacts. Using this store
enables us to avoid loading or parsing the artifacts multiple times. To use
the store, simply import the module directly.

>>> import artefacts.state

"""

# We'll need to think a lot more about how to handle state if we ever want to run
# artefacts on a server. The server might want to load artifacts from different users
# so this kind of state mechanism won't work, because the different users will override
# each other.

import typing
_state = dict()


def set(key: str, value: typing.Any) -> typing.Union[typing.Any, None]:
    """
    Places an object in the store.

    >>> artefacts.state.set('myitem', {'a': 1})
    {'a': 1}

    """
    
    _state[key] = value
    return _state[key]


def get(key: str) -> typing.Union[typing.Any, None]:
    """
    Returns an object from the store, if it exists.

    >>> result = artefacts.state.set('myitem', {'a': 1})
    >>> artefacts.state.get('myitem')
    {'a': 1}

    """

    return _state.get(key)


def exists(key: str) -> bool:
    """
    Returns `True` if the key exists in the store.

    >>> result = artefacts.state.set('myitem', {'a': 1})
    >>> artefacts.state.exists('myitem')
    True
    >>> artefacts.state.exists('thisdoesnotexist')
    False

    """
    return key in _state


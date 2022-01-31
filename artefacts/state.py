"""
Module for storing state of loaded and parsed artifacts, so that we don't
need to perform multiple loads or parsing.
"""


def get(key):
    return globals().get(key)


def set(key, value):
    globals()[key] = value
    return globals()[key]


def exists(key):
    return key in globals()


def get_or_set(key, value):
    return get(key) or set(key, value)

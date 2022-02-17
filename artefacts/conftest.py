# This confest.py file is used for configuring the doctests in the package. It
# needs to be contained in the base of the package's directory for pytest to
# to correctly create the fixtures used in the doctests.

import pytest


@pytest.fixture(autouse=True, scope='session')
def add_artefacts(doctest_namespace):
    import artefacts
    doctest_namespace["artefacts"] = artefacts

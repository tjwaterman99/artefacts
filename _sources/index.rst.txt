.. artefacts documentation master file, created by
   sphinx-quickstart on Tue Feb  1 07:54:40 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

artefacts
=========

`A python deserialization library for dbt artifacts.`

Introduction
------------

The artefacts API aims to provide simple, easy to use, well documented Python objects for dbt's artifacts [#f1]_ [#f2]_. The API makes it easier to build functionality on top of your dbt project, such as linters, CI/CD runners, and many other features.

Here's an example that shows how to use the API to check that all models have at least 1 test.

.. code-block:: python

  >>> import artefacts.api
  >>> models = artefacts.api.models()
  >>> for model in models:
  ...   assert len(model.tests) > 0

There are many other methods in the :code:`artefacts.api` that make it easy to interact with your dbt project. You can find usage examples in the :ref:`api` documentation as well as detailed information about the various objects returned by the API inside the :ref:`reference` section.

To get started, please see the :ref:`installation` instructions. We also provide a :ref:`tutorial` that demonstrates how to use artefacts to build a "conventions linter" for your dbt project.

Alternatives
------------

There are basically two alternatives to artefacts: using the :code:`json.load` function to load the artifacts into primitive Python objects, or using the :code:`dbt-core` functions for loading artifacts.

**Using** :code:`json.load`
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The native json parsing is easy to use, but is inconvenient for even moderate use cases. For example, to identify all the tests associated with a model in the above example would require about 50 lines of code, including logic for handling edge cases.

A simpler approach is to use a json deserialization library like :code:`pydantic`, which handles converting the simple dictionary into a Python object. 

**Using** :code:`dbt-core`
~~~~~~~~~~~~~~~~~~~~~~~~~~

The dbt-core library is likely the better long term solution to using artifacts once dbt provides a Python API. 

But currently dbt does not support using Python to interact with your dbt project, which means there is no documentation for using the various Python objects, and you'd need to read and understand the complex Python source code to accomplish even simple tasks like listing the models in your project.

.. toctree::
   :maxdepth: 2
   :hidden:

   install
   tutorial
   api
   reference
   config

.. rubric:: Footnotes

.. [#f1] See the dbt documentation for more details about the various types of dbt artifacts and how they are generated: https://docs.getdbt.com/reference/artifacts/dbt-artifacts
.. [#f2] See https://schemas.getdbt.com for more details about the specific data contained in the dbt artifacts 

.. toctree::
   :maxdepth: 2
   :hidden:

   api
   reference
   config
   alternatives


artefacts
=========

`A python deserialization library for dbt artifacts.`

.. code-block::

    pip install artefacts


Introduction
------------

The artefacts API aims to provide a set of simple, well documented Python objects for building functionality into your dbt project. The project's goal is to make it easier to build features including linters, CI/CD runners, notifications, and others.

Here's an example that shows how to use the API to check that all models in a dbt project have at least 1 test.

.. code-block:: python

  >>> import artefacts.api
  >>> models = artefacts.api.models()
  >>> for model in models:
  ...   assert len(model.tests) > 0

Please see the :ref:`api` documentation for a full list of all methods exposed by the API, as well as the :ref:`reference` section for detailed information about the various objects that the API returns.

There are several alternatives to using artefacts, and we discuss their trade-offs in the :ref:`alternatives` section.

To get started, please see the :code:`Usage` section in the project's `README on Github <https://github.com/tjwaterman99/artefacts#usage>`_
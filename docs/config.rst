Configuration
=============

artefacts can be configured through environment variables, a `pyproject.toml` file, or passing a :code:`Config` object to each deserializer.

If the same configuration value is set in multiple locations, artefacts will select the value in this order:

- :code:`Config` objects passed to the deserializer
- Environment variables
- Values set in a `pyproject.toml` file

.. warning::

    When using the :code:`Config` object to pass configuration to a deserializer, usage of all deserializers will continue
    to use the same config.

    **In other words, you can only set your configuration before using a deserializer for the first time,** and you cannot change a configuration value once a deserializer has been initalized.

.. note::

    Artefacts will parse environment variables that begin with :code:`ARTEFACTS_`. 
    
    For example, to set the configuration option :code:`dbt_project_dir` with an environment variable, use the value :code:`ARTEFACTS_DBT_PROJECT_DIR`.


The following configuration options are supported.

:code:`dbt_project_dir`
~~~~~~~~~~~~~~~~~~~~~~~

The directory that artefacts will search for your dbt project. Defaults to the current working directory (:code:`.`).

.. code-block:: python

    >>> from artefacts import Config, Manifest
    >>> config = Config(dbt_project_dir='dbt_projects/poffertjes_shop')
    >>> manifest = Manifest(config=config)


.. code-block:: shell

    $ export ARTEFACTS_DBT_PROJECT_DIR=dbt_projects/poffertjes_shop


.. code-block:: toml

    # pyproject.toml
    [artefacts]
    dbt_project_dir = "dbt_projects/poffertjes_shop"


:code:`dbt_target_dir`
~~~~~~~~~~~~~~~~~~~~~~

The directory that artefacts will search for your compiled artifacts, relative to :code:`$DBT_PROJECT_DIR`. Defaults to :code:`target`.

.. code-block:: python

    >>> from artefacts import Config, Manifest
    >>> config = Config(dbt_target_dir='target')
    >>> manifest = Manifest(config=config)


.. code-block:: shell

    $ export ARTEFACTS_DBT_TARGET_DIR=target


.. code-block:: toml

    # pyproject.toml
    [artefacts]
    dbt_target_dir = "target"

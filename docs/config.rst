Configuration
=============

artefacts can be configured through environment variables or a `pyproject.toml` file.

The following configuration options are supported.

dbt project directory
~~~~~~~~~~~~~~~~~~~~~

The directory that artefacts will search for your dbt project. Defaults to the current working directory (:code:`os.getcwd()`).

.. code-block:: shell

    $ export DBT_PROJECT_DIR=dbt_projects/poffertjes_shop


.. code-block:: toml

    # pyproject.toml
    [artefacts]
    dbt_project_dir = "dbt_projects/poffertjes_shop"


dbt target directory
~~~~~~~~~~~~~~~~~~~~

The directory that artefacts will search for your compiled artifacts, relative to :code:`$DBT_PROJECT_DIR`. Defaults to :code:`target`.

.. code-block:: shell

    $ export DBT_TARGET_DIR=target


.. code-block:: toml

    # pyproject.toml
    [artefacts]
    dbt_target_dir = "target"

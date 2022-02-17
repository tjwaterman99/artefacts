Alternatives
------------

artefacts is built on top of dbt's artifacts [#f1]_ [#f2]_, so there are several trade-offs compared to using other approaches for working with your dbt project. We discuss some of the trade-offs associated with those alternatives below.

**Using** :code:`dbt-core`
~~~~~~~~~~~~~~~~~~~~~~~~~~

The dbt-core library is likely the better long term solution to using artefacts, and is already being used by projects like `fal <https://github.com/fal-ai/fal>`_.

But currently dbt does not provide first-class support for using a Python to interact with your dbt project [#f3]_. 

The lack of first-class support means there is no documentation for using the various Python objects exposed by the library, so you'll need to read and understand the complex Python source code to accomplish simple tasks like iterating over the models in your project.

The lack of Python support also means that the dbt-core library does not expose many *convenience* methods for the objects it publishes. While it is possible to use dbt-core for many of the same tasks as artefacts, we hope to make it easier to accomplish those tasks.

Eventually we expect that features like the work-in-progress `dbt.lib <https://github.com/dbt-labs/dbt-core/blob/main/core/dbt/lib.py>`_ will eventually supplant the benefits of a 3rd party library like artefacts. But until features like that are fully released, we feel a library like artefacts can be useful for analytics engineers that want to start building new functionality into their dbt projects today.


**Using** dbt's :code:`jinja` context
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Another way to interact programmatically with your dbt project is by using the Jinja context available to a dbt model. This is the approach taken by some dbt packages including `dbt_meta_testing <https://hub.getdbt.com/tnightengale/dbt_meta_testing/latest/>`_.

The Jinja context contains python objects like `graph <https://docs.getdbt.com/reference/dbt-jinja-functions/graph>`_, which can be used for accomplishing tasks like identifying the models in your project that are missing documentation.  

But using the Jinja context is often more complex than it might seem. Compare the following two code examples, both of which print the models in a specific package that have an incremental materialization.

.. code-block:: python

    {% if execute %}
    {% for node in graph.nodes.values()
        | selectattr("resource_type", "equalto", "model")
        | selectattr("package_name", "equalto", "snowplow") %}
    
        {% do log(node.unique_id ~ ", materialized: " ~ node.config.materialized, info=true) %}
    
    {% endfor %}
    {% endif %}


.. code-block:: python

    import artefacts.api
    for model in artefacts.api.models();
        if (
                model.package_name == 'snowplow' and 
                model.config.materialized == 'table'
        ):
                print(f"{model.unique_id} ~ materialized: {model.config.materialized}")

While an "embedded" language like Jinja is fantastic for features like writing SQL macros, it is challenging to use for moderately complex use cases. We feel that using Python can often make it easier and more maintainable to program new functionality into your project.

**Using** :code:`json.load`
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The last way we'll discuss for programmatically interacting with your dbt project is by using the raw artifacts directly. 

You can load and parse the raw artifacts with Python's built in :code:`json` library.

.. code-block:: python

    import json
    
    with open('target/manifest.json') as fh:
        manifest = json.load(fh)

The :code:`manifest` above is a simple Python dictionary, and that approach is probably the simplest possible for various scripts.

A deserialization library like artefacts essentially extends this approach, by converting that simple Python dictionary :code:`manifest` into a more full-featured Python object. 

The more full-featured Python object can then make it trivial to perform tasks like traversing the graph of dbt nodes. For example, you can easily pull data from the :code:`catalog` into an object from the manifest.

.. code-block:: python

    import artefacts.api

    model = artefacts.api.models()[0]

    for column_name, column_details in model.catalog.columns.items():
        print(column_name, column_details.node_type)


.. rubric:: Footnotes

.. [#f1] See the dbt documentation for more details about the various types of dbt artifacts and how they are generated: https://docs.getdbt.com/reference/artifacts/dbt-artifacts. You can also find a quick intro to more types of functionality that you can build with dbt artifacts in this excellent blog post on `guitton.io <https://guitton.co/posts/dbt-artifacts>`_ .
.. [#f2] See https://schemas.getdbt.com for more details about the specific data contained in the dbt artifacts 
.. [#f3] See the dbt notes about using Python to work with a dbt project: https://docs.getdbt.com/docs/running-a-dbt-project/dbt-api



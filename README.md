# artefacts

_A deserialization library for dbt artifacts._

```
pip install artefacts
```

The `artefacts.api` module aims to provide simple, easy to use python objects for interacting with your dbt project. Here's an example that identifies models in your project that are missing tests or descriptions.

```py
>>> import artefacts.api
>>> for model in artefacts.api.models():
...     if model.description is None or len(model.tests) == 0:
...         print(f"Incomplete model: {model.name}")

```

### Usage

After installing artefacts, you first need to _compile_ your dbt project.

```
dbt compile
```

You can then start using the api.

```py
>>> import artefacts.api
```

### Docs

Documentation for all methods of the api is available on this project's Github Pages site.

> https://tjwaterman99.github.io/artefacts/

References for the objects returned by the api is available in the References section.

> https://tjwaterman99.github.io/artefacts/reference.html

### Development Setup

Open this repository in a Github Codespace. (Click the green `Code` button in the repository's [Github page](https://github.com/tjwaterman99/artefacts) and select `New Codespace`).

#### Testing

```
poetry run pytest
```

By default, pytest will test against the dbt project located at `DBT_PROJECT_DIR`. To test against a different dbt project, update that environment variable and build the project.

```
export DBT_PROJECT_DIR=$PWD/dbt_projects/dbt-starter-project
poetry run dbt build --project-dir $DBT_PROJECT_DIR
poetry run pytest
```

#### Documentation site

Use `sphinx-livereload` to run the docs site on port `8000`.

```
poetry run sphinx-autobuild docs/ docs/_build
```
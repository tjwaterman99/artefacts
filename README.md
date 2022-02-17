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

Documentation for the project is available on the Github Pages site.

> https://tjwaterman99.github.io/artefacts/

All methods exposed by the api are documented with usage examples in the API section.

> https://tjwaterman99.github.io/artefacts/api.html

References for the objects returned by the api are available in the References section.

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

To run the doctests use the `--doctest-modules` flag. Note that the doctests are intended to pass only when using the [`poffertjes_shop`](https://github.com/tjwaterman99/poffertjes_shop) project.

```
poetry run pytest --doctest-modules
```

#### Documentation site

Use `sphinx-livereload` to run the docs site on port `8000`.

```
poetry run sphinx-autobuild docs/ docs/_build --watch artefacts
```
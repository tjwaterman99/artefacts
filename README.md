# artefacts

A deserialization library for dbt artifacts.

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
#!/bin/bash

# This command is ran during the devcontainer's `postCreateCommand` step
# every time the container is built.

apt-get update
apt-get install -y postgresql
sudo service postgresql start
sudo -u postgres psql -c "create user $PGUSER with password '$PGPASSWORD'"
sudo -u postgres createdb $PGDATABASE -O $PGUSER

pipx install poetry
poetry install
git submodule update --init --recursive

rm -rf dbt_projects/starter_project  # If rebuilding the devcontainer, need to clean this for the setup command to work
poetry run dbt init starter_project --skip-profile-setup && mv starter_project dbt_projects/
poetry run dbt deps --project-dir $ARTEFACTS_DBT_PROJECT_DIR
poetry run dbt build --project-dir $ARTEFACTS_DBT_PROJECT_DIR
poetry run dbt docs generate --project-dir $ARTEFACTS_DBT_PROJECT_DIR
poetry run dbt source freshness --project-dir $ARTEFACTS_DBT_PROJECT_DIR

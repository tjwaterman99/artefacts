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

poetry run dbt build --project-dir $DBT_PROJECT_DIR

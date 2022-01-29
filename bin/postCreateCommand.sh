#!/bin/bash

# This command is ran during the devcontainer's `postCreateCommand` step
# every time the container is built.

apt-get update
apt-get install -y postgresql
sudo service postgresql start
sudo -u postgres psql -c "create user artefacts with password 'password'"
sudo -u postgres createdb artefacts -O artefacts

pipx install poetry
poetry install
git submodule update --init --recursive

poetry run dbt build --project-dir $DBT_PROJECT_DIR

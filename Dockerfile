FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

ENV PGHOST=localhost
ENV PGPASSWORD=password
ENV PGUSER=artefacts
ENV PGDATABASE=artefacts
ENV DBT_PROFILES_DIR=$PWD/dbt_projects
ENV DBT_PROJECT_DIR=$PWD/dbt_projects/jaffle_shop

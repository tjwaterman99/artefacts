#!/bin/bash

# This command is ran during the devcontainer's `postCreateCommand` step
# every time the container is built.

pipx install poetry
poetry install
git submodule update --init --recursive
# Validate that the dbt_projects have been initialized.

import os


def test_dbt_projects_exist():
    for dirpath in os.listdir('dbt_projects'):
        dbt_project = os.path.join('dbt_projects', dirpath)
        if os.path.isdir(dbt_project):
            assert len(os.listdir(dbt_project)) > 0
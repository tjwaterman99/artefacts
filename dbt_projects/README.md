# dbt_projects configuration

This directory contains git repos that point to dbt projects. 

### Adding a new submodule

To add a new dbt project, use `git submodule add`.

```
git submodule add https://github.com/dbt-labs/dbt-starter-project dbt_projects/dbt-starter-project
```

Then update the `dbt_projects/profiles.yml` file with a new profile for the project.

### Syncing changes from the submodule's source

If a submodule's source changes, you need to manually update the submodule to use the new commits.

To change the commit that an existing submodule uses, first navigate to that submodule's directory.

```
cd dbt_projects/dbt-start-project
```

Pull the latest changes from the remote and checkout the specific commit.

```
git pull
git checkout ...
```

Navigate back to the _root_ of the parent repo (ie the root of the `artefacts` repo).

```
cd ../..
```

You should see that there "new commits" detected in the submodule when using `git status`.

```
git status
```
```
modified:   dbt_projects/dbt-starter-project (new commits)
```

Add those "new commits" and commit them to the parent repository.

```
git add -A
git commit -m "Update submodule"
```

### Keeping local submodules in sync with `main`

If the `main` branch of this repository updates the commit that a submodule uses, you need to manually instruct git to switch any existing submodule to use that commit.

Merge the changes from `main` into your branch.

```
git checkout main
git pull
git checkout dev/mybranch
git merge main
```

Update the submodules.

```
git submodule update --init --recursive
```

The version of the submodules in your project should now match the version in the `main` branch.

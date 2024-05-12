# template-py

Python template repository

* [Rye](https://rye-up.com/)

## Run app

Sync the project; e.g. install dependencies, etc.

```sh
rye sync
```


Run command hello.

```sh
rye run hello
```

## How create this template

Initialize the project

```sh
rye init
```

Edit `project.requires-python` in pyproject.toml to set the required Python version and pin the version of python to use.

```sh
rye pin 3.11
```

Edit ruff configuration in pyproject.toml.

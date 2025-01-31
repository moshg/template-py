# template-py

Python template repository

## Requirements

* [uv](https://docs.astral.sh/uv/)

## Run app

Sync the project; e.g. install dependencies, etc.

```sh
uv sync
```


The hello command is defined in project.scripts in pyproject.toml.

```sh
uv run hello
```

Project management commands are located in Taskfile.yaml.

```sh
task lint
```


## How create this template

Initialize the project

```sh
uv init --package
```

Edit ruff configuration in pyproject.toml.

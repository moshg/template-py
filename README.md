# template-py

Python template repository

## Requirements

* [uv](https://docs.astral.sh/uv/): Python package manager
* [Task](https://taskfile.dev/): Task runner

You can use the provided [dev container](https://code.visualstudio.com/docs/devcontainers/containers) to automatically set up the development environment with all requirements.

## Run app

Sync the project; e.g. install dependencies, etc.

```sh
uv sync
```

Convenient commands are defined in [Taskfile.yaml](Taskfile.yaml). You can run them with:

```sh
# run the main script
task run
# check code quality
task check
```

You can see all available commands with:

```sh
task --list-all
```


## How create this template

Initialize the project

```sh
uv init --package
```

Edit ruff configuration in pyproject.toml.

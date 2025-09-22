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

Commands are located in Taskfile.yaml.

```sh
# run the script
task run
# typecheck and lint
task check
# format
task format
# test
task test
```


## How create this template

Initialize the project

```sh
uv init --package
```

Edit ruff configuration in pyproject.toml.

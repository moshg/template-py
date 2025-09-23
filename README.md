# template-py

Python template repository

## Requirements

* [uv](https://docs.astral.sh/uv/): Python package manager
* [Task](https://taskfile.dev/): Task runner

You can use the provided [dev container](https://code.visualstudio.com/docs/devcontainers/containers) to automatically set up the development environment with all requirements.

## Tech Stack

### Dependencies
- **[Pydantic](https://docs.pydantic.dev/)**: Data validation and settings management using Python type annotations
- **[structlog](https://www.structlog.org/)**: Structured logging for better observability

### Development Tools
- **[uv](https://docs.astral.sh/uv/)**: Fast Python package manager and resolver
- **[Ruff](https://docs.astral.sh/ruff/)**: An extremely fast Python linter and code formatter
- **[Pyright](https://microsoft.github.io/pyright/#/)**: Static type checker for Python
- **[pytest](https://docs.pytest.org/)**: Testing framework for Python
- **[pip-audit](https://github.com/pypa/pip-audit)**: Security vulnerability scanner for Python packages
- **[Task](https://taskfile.dev/)**: Simple task runner

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
uv init --package --build-backend uv
```

Edit some configurations in pyproject.toml.

# demo-dvc-push-bug

Demonstrating a DVC bug with pushing data to remotes in certain circumstances.

## Installation

Please use Python [`poetry`](https://python-poetry.org/) to run and install related content.
The Poetry environment for this project includes dependencies which help run IDE environments, manage the data, and run workflows.

```bash
# after installing poetry, create the environment
poetry install
```

## Development

### Jupyter Lab

Please follow installation steps above and then use a relevant Jupyter environment to open and explore the notebooks under the `notebooks` directory.

```bash
# after creating poetry environment, run jupyter
poetry run jupyter lab
```

### DVC (Data Version Control)

[DVC](https://dvc.org/doc) is used for managing data associated with this project.
The Python package for DVC is included as a dependency within the Poetry environment.
Use the following command to pull the latest data for the project:

```bash
# pull data from DVC data storage defined for this project
poetry run dvc pull
```

### Poe the Poet

We use [Poe the Poet](https://poethepoet.natn.io/index.html) to define and run tasks defined within `pyproject.toml` under the section `[tool.poe.tasks*]`.
This allows for the definition and use of a task workflow when implementing multiple procedures in sequence.

For example, use the following to run the `data_prep` task:

```bash
# run data_prep task using poethepoet defined within `pyproject.toml`
poetry run poe data_prep
```

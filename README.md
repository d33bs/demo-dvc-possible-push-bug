# demo-dvc-possible-push-bug

Demonstrating a possible DVC bug with pushing data to remotes in certain circumstances.

## Installation

Please use Python [`poetry`](https://python-poetry.org/) to run and install related content.
The Poetry environment for this project includes dependencies which help run IDE environments, manage the data, and run workflows.

```bash
# after installing poetry, create the environment
poetry install
```

## Poe the Poet

Use [Poe the Poet](https://poethepoet.natn.io/index.html) to define and run tasks defined within `pyproject.toml` under the section `[tool.poe.tasks*]`.
This allows for the definition and use of a task workflow when implementing multiple procedures in sequence.

For example, use the following to run the `dvc_possible_bug` task:

```bash
# run data_prep task using poethepoet defined within `pyproject.toml`
poetry run poe dvc_possible_bug
```

## Output

There are two files which may help demonstrate the findings: `dvc_list_output_1.txt` and `dvc_list_output_2.txt`.

- `dvc_list_output_1.txt`: shows a listing of files within the dir after data generation, dvc add, and dvc push.
- `dvc_list_output_2.txt`: shows a listing of files within the dir after data removal, and dvc pull.

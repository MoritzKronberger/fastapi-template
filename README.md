# ⚡ FastAPI Template

Template repository for a FastAPI + [Uvicorn](https://www.uvicorn.org/) application with routers. (See [FastAPI - Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/))

Includes setup for strict typechecking with [mypy](https://mypy.readthedocs.io/en/stable/index.html) and linting with [flake8](https://flake8.pycqa.org/en/latest/index.html) + settings for the [VSCode Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

## Installation

__*Uses Python 3.10*__

Create a virtual environment:

```bash
python -m venv venv
```

Active the virtual environment:

```bash
./venv/Scripts/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run Application

Run Uvicorn server with hot reloads:

```bash
uvicorn app.main:app --reload
```

Access the docs at [http://127.0.0.1:8000/docs] or the alternative docs at [http://127.0.0.1:8000/redoc].

## Run Typechecks and Linter

Run mypy for typechecks:

```bash
mypy -m app
```

Run flake8 for linting:

```bash
flake8
```

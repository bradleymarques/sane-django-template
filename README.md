# Sane Django Template <!-- omit in toc -->

- [Current Feature Set](#current-feature-set)
- [Installing](#installing)
- [Environment Variables](#environment-variables)
- [Useful Scripts](#useful-scripts)
- [Testing](#testing)

A sane template to use as the starting point when creating [Django](https://www.djangoproject.com/) web apps.

## Current Feature Set

- 🐳 Container-first (using Docker)
- 🎨 Bootstrap 5.3 with [django-libsass](https://github.com/torchbox/django-libsass) and [django-compressor](https://github.com/django-compressor/django-compressor)
- 🏡 There is a single static page (home)
- 📧 Users can register on the site registration with email verification
- 🔐 Change password and forgot password flow in case of forgotten password
- 🔑 Per-record authorization using [django-rules](https://github.com/dfunckt/django-rules)
- 📸 Users can upload a profile image
- 🌗 User preferences page to pick between dark mode, light mode, and auto
- 🧪 Tests with Pytest
- 🐙 GitHub action to automate tests
- 🔃 Pre-commit hooks
  - [black](https://github.com/psf/black)
  - [pycln](https://hadialqattan.github.io/pycln/)
  - [isort](https://pycqa.github.io/isort/)

## Installing

1. First, install [Poetry](https://python-poetry.org/docs/#installation).
2. (Optional) Configure Poetry to create a .venv environment in the project:

    ```zsh
    poetry config virtualenvs.create true
    poetry config virtualenvs.in-project true
    ```

3. Run this (will create a `.venv` folder in the project directory, and this folder is gitignored):

    ```zsh
    poetry install
    ```

4. Install pre-commit hooks:

    ```zsh
    pre-commit install
    ```

## Environment Variables

Before starting the server, copy the contents of file `.env.example` to `.env`.
This file contains the environment variables and is gitignored.

When making additions/changes to this file, also add the variables to `pytest.ini` which passes these to the application when testing.

## Useful Scripts

To save on typing, I have included the following useful scripts:

| Command                             | Description                                                         |
| ----------------------------------- | ------------------------------------------------------------------- |
| `./scripts/up.sh`                   | Build and start the server (detached) on <localhost:8000>           |
| `./scripts/down.sh`                 | Stop the server                                                     |
| `./scripts/down_up.sh`              | Runs down.sh then up.sh                                             |
| `./scripts/shell.sh`                | Run a Django shell                                                  |
| `./scripts/seed.sh`                 | Seeds the database                                                  |
| `./scripts/regenerate_db_schema.sh` | Deletes all migrations, makes migrations, migrates and seeds the db |

You can open the scripts to see what they do, but they basically mostly call `docker compose`.

Note you can also run the server without Docker with:

```zsh
python manage.py runserver
```

## Testing

```zsh
poetry shell
pytest
```

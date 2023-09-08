# Sane Django Template <!-- omit in toc -->

- [Current (and planned) Feature Set](#current-and-planned-feature-set)
  - [Authentication](#authentication)
  - [Authorization](#authorization)
  - [Community](#community)
  - [Notifications](#notifications)
  - [Styling](#styling)
  - [Other](#other)
- [Installing](#installing)
- [Environment Variables](#environment-variables)
- [Useful Scripts](#useful-scripts)
- [Testing](#testing)
- [Other commands](#other-commands)

A sane, feature-rich template for creating [Django](https://www.djangoproject.com/) web apps.

## Current (and planned) Feature Set

### Authentication

- [x] Site registration with email verification
- [x] Reset/forgot password flow in case of forgotten password
- [ ] Two-factor authentication using an authentication app such as "Authy" or "Google Authenticator"

### Authorization

- [x] Per-record authorization using [django-rules](https://github.com/dfunckt/django-rules)

### Community

- [x] Users can upload a profile image
- [x] Comment system
- [ ] Voting system (possibly using [django-voting](https://github.com/jazzband/django-voting))
- [ ] Users can report abusive content and admins can review and remove the content
- [ ] Admins can ban users
- [ ] Audits for admins (possibly using [django-reversion](https://django-reversion.readthedocs.io/en/latest/))
- [ ] Private messaging with real-time communication (possibly using [django-channels](https://github.com/django/channels))

### Notifications

- [ ] In-app
- [ ] EMail

### Styling

- [x] Bootstrap 5.3 with [django-libsass](https://github.com/torchbox/django-libsass) and [django-compressor](https://github.com/django-compressor/django-compressor) meaning easy theme customisation using scss
- [x] User preferences page to pick between dark mode, light mode, and auto

### Other

- [x] Testing using Pytest, and GitHub action to automate tests
- [x] Container-first (using Docker)
- [x] Pre-commit hooks

## Installing

1. First, install [Poetry](https://python-poetry.org/docs/#installation).
2. (Optional) Configure Poetry to create a .venv environment in the project:

    ```zsh
    poetry config virtualenvs.create true
    poetry config virtualenvs.in-project true
    ```

3. Run:

    ```zsh
    poetry install
    ```

The final command will create a `.venv` folder in the project directory, and this folder is gitignored.

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

## Testing

```zsh
source .venv/bin/activate
pytest
```

## Other commands

Starting a new Django app: `poetry run python manage.py startapp <NEW_APP_NAME>`

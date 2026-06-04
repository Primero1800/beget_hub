# beget_hub

Hub site for [primero1800.ru](https://primero1800.ru) — a Django application that lists independent sub-projects, each living on its own subdomain.

## Stack

- **Django 6** — web framework
- **SQLite** — database
- **django-modeltranslation** — RU/EN i18n
- **WhiteNoise** — static file serving
- **Phusion Passenger** — WSGI on Beget shared hosting
- **Poetry** — dependency management
- **GitHub Actions** — CI (ruff, mypy, pytest) + auto-deploy on merge to `main`

## Local setup

```bash
git clone https://github.com/Primero1800/beget_hub.git
cd beget_hub

poetry install
cp .env.example .env   # fill in SECRET_KEY

poetry run python manage.py migrate
poetry run python manage.py createsuperuser
poetry run python manage.py runserver
```

Open [http://localhost:8000/ru/](http://localhost:8000/ru/)

## Project management

Sub-projects are managed via Django admin at `/admin/` → **SubProject**.

Each entry has:
- **Name** (RU + EN) — displayed on the card
- **URL** — link to the subdomain (e.g. `https://mirror.primero1800.ru`)
- **Description** (RU + EN) — shown below the name
- **Preview images** — up to 9 images uploaded via inline, displayed as a 3×3 collage
- **Order** — sort order on the page
- **Active** — toggle visibility

## Running checks

```bash
poetry run ruff check .          # linting
poetry run mypy apps/ hub_config/  # type checking
poetry run pytest                # tests with coverage
```

## Deployment

Auto-deploys to [primero1800.ru](https://primero1800.ru) on every merge to `main` via GitHub Actions + SSH.

Required GitHub secret: `BEGET_PASSWORD`

## Sub-projects

| Project | URL |
|---------|-----|
| Mirror | [mirror.primero1800.ru](https://mirror.primero1800.ru) |

## Version

Current: `0.2.1` — see [VERSION](VERSION)

# Phonebook API

A small asynchronous REST API (FastAPI + SQLAlchemy async) — a learning project.
It re-implements, in REST, the phone directory service I previously wrote with
raw TCP sockets in C, so the two designs can be compared.

## From sockets to REST

| C project (custom TCP protocol) | This project (HTTP/REST) |
|---|---|
| `LOGIN user pass` | `POST /auth/login` → access token |
| `ADD P Rossi Mario 333...` | `POST /contacts` |
| `SEARCH ross` | `GET /contacts?q=ross` |
| `ERR ... permesso_negato` | `403 Forbidden` |
| bad input handled by hand | `422` generated from Pydantic schemas |
| one `fork`ed process per client | one event loop, `async`/`await` |
| plain-text passwords | argon2 password hashes |

## Stack
FastAPI · Uvicorn · Pydantic v2 · SQLAlchemy 2.0 (async) + SQLite (aiosqlite) · PyJWT · argon2-cffi · pytest + httpx

## Run

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload     # interactive docs: http://127.0.0.1:8000/docs
pytest
```

## Layout

```
app/
  main.py          app factory, lifespan, /health
  config.py        settings from environment variables
  db.py            async engine, session, get_db dependency
  models.py        ORM tables (what is stored)
  schemas.py       Pydantic models (what the API accepts/returns)
  security.py      hashing, tokens, permission checks
  routers/         contacts.py, auth.py
tests/             pytest, in-memory database per test
```

## Roadmap

- [x] 1. Project skeleton, `/health`, OpenAPI docs
- [ ] 2. Schemas and validation (done in `schemas.py`; understand and extend)
- [ ] 3. Database CRUD with async SQLAlchemy
- [ ] 4. Search (`?q=`) and pagination
- [ ] 5. Authentication, read/write permissions, password hashing
- [ ] 6. Tests, Dockerfile, GitHub Actions CI

## Security notes
- Secrets come from environment variables, never from the repo.
- Passwords are hashed (argon2); responses never include hashes.
- Input is validated at the boundary (Pydantic) and queries are parameterised (SQLAlchemy).
- Login errors do not reveal whether a username exists.

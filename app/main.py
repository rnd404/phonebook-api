from contextlib import asynccontextmanager

from fastapi import FastAPI

from app import models  # noqa: F401  (registers the tables on Base.metadata)
from app.db import Base, engine
from app.routers import auth, contacts


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Development convenience: create tables at startup.
    # Real projects use migrations (Alembic) instead.
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()


app = FastAPI(title="Phonebook API", version="0.1.0", lifespan=lifespan)
app.include_router(contacts.router)
app.include_router(auth.router)


@app.get("/health", tags=["meta"])
async def health() -> dict[str, str]:
    return {"status": "ok"}

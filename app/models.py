"""Database tables (SQLAlchemy 2.0 typed style).

These are NOT the API schemas: what is stored and what is exposed are
deliberately separate (e.g. password_hash must never leave the server).
"""
from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(primary_key=True)
    kind: Mapped[str] = mapped_column(String(10))            # "person" | "company"
    name: Mapped[str] = mapped_column(String(80), index=True)
    surname: Mapped[str | None] = mapped_column(String(80), index=True)  # persons only
    phone: Mapped[str] = mapped_column(String(20))


class User(Base):
    """Mirrors data/utenti.txt of the C project: R / W / RW permissions."""
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    can_read: Mapped[bool] = mapped_column(Boolean, default=True)
    can_write: Mapped[bool] = mapped_column(Boolean, default=False)

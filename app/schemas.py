"""API contract: what clients send and receive (Pydantic v2)."""
from typing import Literal, Self

from pydantic import BaseModel, ConfigDict, Field, model_validator

PHONE_PATTERN = r"^\+?[0-9 ]{6,20}$"


class ContactCreate(BaseModel):
    kind: Literal["person", "company"]
    name: str = Field(min_length=1, max_length=80)
    surname: str | None = Field(default=None, min_length=1, max_length=80)
    phone: str = Field(pattern=PHONE_PATTERN)

    @model_validator(mode="after")
    def surname_rules(self) -> Self:
        # Cross-field validation: the same rule the C server enforced by hand.
        if self.kind == "person" and self.surname is None:
            raise ValueError("surname is required for a person")
        if self.kind == "company" and self.surname is not None:
            raise ValueError("a company has no surname")
        return self


class ContactRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)  # build from ORM objects

    id: int
    kind: Literal["person", "company"]
    name: str
    surname: str | None
    phone: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=8, max_length=128)
    can_read: bool = True
    can_write: bool = False


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    can_read: bool
    can_write: bool
    # note: no password / password_hash field here, on purpose

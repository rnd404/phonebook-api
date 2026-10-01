"""Authentication endpoints.  (STEP 5)"""
from fastapi import APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm  # noqa: F401  (used in step 5)

from app.schemas import Token

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=Token)
async def login():
    """TODO(step 5): accept OAuth2PasswordRequestForm via Depends(), check the
    user and password, return a Token.  Wrong credentials -> 401 with the SAME
    message whether the user exists or not (no user enumeration)."""
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, "Not implemented yet")

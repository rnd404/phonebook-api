"""Password hashing, tokens and permission checks.  (STEP 5)

Everything here is a stub: the signatures are fixed, the bodies are ours to write.
"""
from collections.abc import Callable

from app.models import User


def hash_password(password: str) -> str:
    """TODO(step 5): argon2 hash (argon2.PasswordHasher). Never store plain text."""
    raise NotImplementedError


def verify_password(password: str, password_hash: str) -> bool:
    """TODO(step 5): verify against the stored hash, return False on mismatch."""
    raise NotImplementedError


def create_access_token(username: str) -> str:
    """TODO(step 5): JWT with 'sub' and 'exp', signed with config.SECRET_KEY."""
    raise NotImplementedError


async def get_current_user() -> User:
    """TODO(step 5): FastAPI dependency. Read the Bearer token, decode it,
    load the user, raise 401 if anything is wrong."""
    raise NotImplementedError


def require_permission(permission: str) -> Callable:
    """TODO(step 5): dependency factory, permission is "read" or "write".
    Raise 403 when the user lacks it (the REST version of auth.c)."""
    raise NotImplementedError

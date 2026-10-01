"""Settings read from environment variables (12-factor style)."""
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./phonebook.db")

# Needed from step 5 (JWT signing). No default on purpose: a hard-coded
# secret in the repo would be a vulnerability. Generate one with:
#   python -c "import secrets; print(secrets.token_urlsafe(32))"
SECRET_KEY = os.getenv("SECRET_KEY")
ACCESS_TOKEN_MINUTES = int(os.getenv("ACCESS_TOKEN_MINUTES", "30"))

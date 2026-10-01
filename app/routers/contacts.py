"""Contact endpoints.

The contract (paths, verbs, status codes, schemas) is complete and visible in /docs.
The bodies are TODOs and answer 501 until implemented.
"""
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_db
from app.schemas import ContactCreate, ContactRead

router = APIRouter(prefix="/contacts", tags=["contacts"])

NOT_YET = HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented yet")


@router.post("", response_model=ContactRead, status_code=status.HTTP_201_CREATED)
async def create_contact(data: ContactCreate, db: AsyncSession = Depends(get_db)):
    """TODO(step 3): insert a Contact, commit, refresh, return it.
    TODO(step 5): require the 'write' permission."""
    raise NOT_YET


@router.get("", response_model=list[ContactRead])
async def search_contacts(
    q: str | None = Query(default=None, min_length=1, max_length=80),
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    db: AsyncSession = Depends(get_db),
):
    """TODO(step 4): case-insensitive substring search on name/surname (ilike),
    ordered, with limit/offset pagination.  No q -> list everything (paginated).
    TODO(step 5): require the 'read' permission."""
    raise NOT_YET


@router.get("/{contact_id}", response_model=ContactRead)
async def get_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    """TODO(step 3): 404 if it does not exist."""
    raise NOT_YET


@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    """TODO(step 3): 404 if missing, otherwise delete.
    TODO(step 5): require the 'write' permission."""
    raise NOT_YET

"""Handle hello routes."""

from fastapi import APIRouter

router = APIRouter()


@router.get('/hello_world', tags=['hello'])
def hello_world(name: str | None = None) -> str:
    """Says Hello."""
    return f'Hello {name or "World"}!'

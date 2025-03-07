from typing import List

from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import db_helper
from app.books import schemas
from app.books import crud


router = APIRouter(tags=["Book"])


@router.get("/")
async def book_list(
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> List[schemas.ReadBook]:
    result = await crud.get_books(session)
    return result


@router.post("/", response_class=RedirectResponse)
async def create_book(
    request: Request,
    book: schemas.Book,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    await crud.create_book(book, session)
    redirect_url = request.url_for("book_list")
    return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)


@router.patch("/{idx}")
async def update_book(
    request: Request,
    idx: int,
    new_data: schemas.UpdateBook,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    await crud.update_book(idx, new_data, session)
    redirect_url = request.url_for("book_list")
    return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)


@router.delete("/{idx}")
async def delete_book(
    request: Request,
    idx: int,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    await crud.delete_book(idx, session)
    redirect_url = request.url_for("book_list")
    return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)

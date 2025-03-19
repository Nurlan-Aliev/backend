from typing import List

from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import db_helper
from app.books import schemas
from app.books import crud
from pydantic import AnyUrl


router = APIRouter(tags=["Book"])


@router.get("/")
async def book_list(
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> List[schemas.ReadBook]:
    result = await crud.get_books(session)
    return result


@router.post("/")
async def create_book(
    book: schemas.Book,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    book.img_url = AnyUrl(
        # "https://img.freepik.com/free-vector/hand-drawn-flat-design-stack-books-illustration_23-2149341898.jpg"
        'https://sun9-54.userapi.com/impg/kzJsESyTsnBXGH4qF1n3db9tvWjWiDCeNOf7FA/eBKoqYGEflU.jpg?size=1439x2160&quality=95&sign=c6a1d23c60234d8cf1b1b80a02b39e4e&type=album'
    )
    await crud.create_book(book, session)
    return "book was created"


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

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.books.models import Books
from app.books import schemas


async def get_books(session: AsyncSession):
    stmt = select(Books)
    user = await session.scalars(stmt)
    return user.all()


async def get_book(idx: int, session: AsyncSession) -> Books:
    stmt = select(Books).where(Books.id == idx)
    my_book = (await session.scalars(stmt)).first()
    return my_book


async def create_book(data: schemas.Book, session: AsyncSession):

    data_dict = data.model_dump()
    data_dict["img_url"] = str(data_dict["img_url"])
    new_book = Books(**data_dict)
    session.add(new_book)
    await session.commit()


async def update_book(
    idx: int,
    data: schemas.UpdateBook,
    session: AsyncSession,
):
    my_book = await get_book(idx, session)
    my_book.title = data.title if data.title else my_book.title
    my_book.author = data.author if data.author else my_book.author
    my_book.phrases = data.phrases if data.phrases else my_book.phrases
    my_book.img_url = str(data.img_url) if data.img_url else my_book.img_url
    await session.commit()


async def delete_book(
    idx: int,
    session: AsyncSession,
):
    my_book = await get_book(idx, session)
    await session.delete(my_book)
    await session.commit()

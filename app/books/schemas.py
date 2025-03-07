from pydantic import BaseModel, AnyUrl


class Book(BaseModel):
    title: str
    author: str
    phrases: str
    img_url: AnyUrl


class ReadBook(Book):
    id: int


class UpdateBook(Book):
    title: str | None = None
    author: str | None = None
    phrases: str | None = None
    img_url: AnyUrl | None = None

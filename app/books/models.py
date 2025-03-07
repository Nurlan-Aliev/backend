from sqlalchemy.orm import Mapped

from app.database import Base


class Books(Base):
    title: Mapped[str]
    author: Mapped[str]
    phrases: Mapped[str]
    img_url: Mapped[str]

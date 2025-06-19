from datetime import datetime
from sqlalchemy import func, Table, Column, ForeignKey, String
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.dialects.postgresql import ARRAY


class BaseClass(DeclarativeBase):
     _id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
     _created: Mapped[datetime] = mapped_column(
         insert_default=func.now(), default=None
     )
     _lastmodified: Mapped[datetime] = mapped_column(default=None, nullable=True, onupdate=datetime.now)



class User(BaseClass):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()


book_author_association_table = Table(
    "book_authors",
    BaseClass.metadata,
    Column("book_id", ForeignKey("books._id"), primary_key=True),
    Column("author_id", ForeignKey("authors._id"), primary_key=True),
)


class Author(BaseClass):
    __tablename__ = "authors"
    name: Mapped[str] = mapped_column()


class Book(BaseClass):
    __tablename__ = "books"

    title: Mapped[str] = mapped_column()
    year: Mapped[int] = mapped_column()
    is_nonfiction: Mapped[bool] = mapped_column()
    image_url: Mapped[str] = mapped_column(nullable=True)
    rating: Mapped[int] = mapped_column(default=1)
    abstract: Mapped[str] = mapped_column(nullable=True)
    summary: Mapped[str] = mapped_column(nullable=True)
    #user_id: Mapped[int] = mapped_column(ForeignKey("users._id"))
    keywords = Column(MutableList.as_mutable(ARRAY(String)))

    authors: Mapped[list[Author]] = relationship(secondary=book_author_association_table)

    def author_string(self) -> str:
        return ", ".join([a.name for a in self.authors])

    @property
    def keyword_string(self) -> str:
        self.keywords.sort()
        return str(self.keywords)



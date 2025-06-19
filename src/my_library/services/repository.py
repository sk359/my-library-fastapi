from collections.abc import Callable
from sqlalchemy import text, select
from sqlalchemy.orm import Session
from fastapi import Depends

from src.my_library.services.db_engine import engine
from src.my_library.classes.orm_classes import Book
from src.my_library.services.session import get_db_session


class Repository:

    def __init__(self, session):
        self.session = session

    def get_book_by_id(self, book_id: int) -> Book:
        with engine.connect() as conn:
            conn.commit()

    def get_all_books(self) -> list[Book]:
        #with Session(engine) as session:
        stmt = select(Book).order_by(Book._id)
        result = self.session.scalars(stmt)
        #print(result.all())
        return result.all()

    def save_new_book(self, book):
        with engine.connect() as conn:
            conn.commit()

    def update_book(self, book):
        with engine.connect() as conn:
            conn.commit()

    def delete_book(self, book):
        with engine.connect() as conn:
            conn.commit()

    def commit(self, close_after_commit=True):
        """
        Commits the session and then closes it
        :return:
        """
        try:
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(e)
        if close_after_commit:
            self.session.close()


#books = get_all_books()
#print(books)

def get_repository() -> Repository:
    session = Session(engine)
    return Repository(session)
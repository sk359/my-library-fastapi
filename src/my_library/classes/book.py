from dataclasses import dataclass

from src.my_library.classes.base import BaseClass


class Book(BaseClass):
    book_id: str
    title: str
    year: int
    author_list: list[str]
    is_nonfiction: bool
    keywords: list[str]
    image_url: str = "http://books.google.com/books/publisher/content?id=iAblDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&imgtk=AFLRE72qy5IsbmllMAYCYGVhS2dQYd8UoONmv52VTRueJqvZ_Z4eTPMpurCNWW-4Vlp77uOZM5X_KT-c8LC-GkzSAmIcPx209BerUUjdvZjoZ-8YOOlTXzfUi2xa3xII_zDscMQxLQOG&source=gbs_api"
    rating: int = 1
    abstract: str = ""
    summary: str = ""

    def author_string(self) -> str:
        return ", ".join(self.author_list)

    @property
    def keyword_string(self) -> str:
        self.keywords.sort()
        return ", ".join(self.keywords)
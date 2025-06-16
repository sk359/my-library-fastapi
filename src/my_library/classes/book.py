from dataclasses import dataclass

@dataclass()
class Book:
    book_id: str
    name: str
    year: int
    author_list: list[str]
    is_nonfiction: bool
    genre: str
    labels: list[str]
    image_url: str = ""
    rating: int = 0
    abstract: str = ""
    summary: str = ""
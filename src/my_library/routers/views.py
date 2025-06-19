import uuid
from typing import Annotated
from fastapi import APIRouter
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

from src.my_library.classes.credentials import Credentials
from src.my_library.classes.book import Book
from src.my_library.classes.enums import NonFictionLabel, FictionLabel
from src.my_library.services.repository import Repository, get_repository

# https://fastapi.tiangolo.com/tutorial/bigger-applications/#apirouter

router = APIRouter()
templates = Jinja2Templates(directory="views")

SessionRepository = Annotated[Repository, Depends(get_repository)]

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="login.html")


@router.get("/new", response_class=HTMLResponse)
async def index(request: Request):
    labels = ["Science-Fiction"]
    labels = FictionLabel.value_list()
    non_fiction_labels = NonFictionLabel.value_list()
    labels.extend(non_fiction_labels)
    labels.sort()
    #return templates.TemplateResponse(request=request, name="new-book.html")
    return templates.get_template("new-book.html").render(dict(request=request, labels=labels))


@router.get("/books/{book_id}", response_class=HTMLResponse)
async def index(request: Request, book_id: str):
    #print("id", book_id)
    #mock_book = Book(book_id=str(uuid.uuid4()), title="Dune", year=1965, author_list=["Frank Herbert"],
    #                is_nonfiction=False,
    #                genre="Roman", keywords=["Science-Fiction"], rating=4,
    #                 abstract="", summary="Epische Erzählung über den Krieg zweier Häuser auf dem Wüstenplaneten Arakis um das Spice")
    #return templates.TemplateResponse(request=request, name="detail-modal.html")
    return templates.get_template("detail-modal.html").render(dict(request=request, book=None))


@router.get("/overview", response_class=HTMLResponse)
async def index(request: Request, repo: SessionRepository):
    #mock_book = Book(book_id=str(uuid.uuid4()), title="Dune", year=1965, author_list=["Frank Herbert"], is_nonfiction=False,
    #                 genre="Science-Fiction", keywords=[], rating=4)
    #books = [mock_book]
    books = repo.get_all_books()
    return templates.get_template("overview.html").render(dict(request=request, books=books))
    #return templates.TemplateResponse(request=request, name="overview.html", books=books)


@router.post("/login", response_class=HTMLResponse)
async def login(request: Request):
    print(request)
    if False:
        return templates.TemplateResponse(request=request, name="login.html")
    #return templates.TemplateResponse(request=request, name="overview.html")
    #return templates.get_template("overview.html").render(dict(request=request, namex="XXX"))
    return RedirectResponse(
        "/overview", status_code=302, headers=None, background=None
    )


#delete => HX-Refresh:true
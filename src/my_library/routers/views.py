import uuid
from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

from ..classes.credentials import Credentials
from ..classes.book import Book

# https://fastapi.tiangolo.com/tutorial/bigger-applications/#apirouter

router = APIRouter()
templates = Jinja2Templates(directory="views")

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="login.html")


@router.get("/new", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="new-book.html")


@router.get("/books/{book_id}", response_class=HTMLResponse)
async def index(request: Request, book_id: str):
    print("id", book_id)
    mock_book = Book(book_id=str(uuid.uuid4()), title="Dune", year=1965, author_list=["Frank Herbert"],
                    is_nonfiction=False,
                    genre="Science-Fiction", labels=[], rating=4)
    #return templates.TemplateResponse(request=request, name="detail-modal.html")
    return templates.get_template("detail-modal.html").render(dict(request=request, book=mock_book))


@router.get("/overview", response_class=HTMLResponse)
async def index(request: Request):
    mock_book = Book(book_id=str(uuid.uuid4()), title="Dune", year=1965, author_list=["Frank Herbert"], is_nonfiction=False,
                     genre="Science-Fiction", labels=[], rating=4)
    books = [mock_book]
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
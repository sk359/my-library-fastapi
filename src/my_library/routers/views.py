from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

# https://fastapi.tiangolo.com/tutorial/bigger-applications/#apirouter

router = APIRouter()
templates = Jinja2Templates(directory="views")

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="login.html")
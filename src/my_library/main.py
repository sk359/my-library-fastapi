from typing import Union
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from .routers.views import router as view_router

app = FastAPI()
app.include_router(view_router)
app.mount("/static", StaticFiles(directory="static"), name="static")
#templates = Jinja2Templates(directory="views")

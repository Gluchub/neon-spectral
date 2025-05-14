from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.requests import Request

templates= Jinja2Templates(directory='selected')

app= FastAPI()
@app.get("/", response_class='/')
async def home(request: Request):
    return templates.TemplateResponse('ghostwirecc.html', {'request':request})

@app.get("/void", response_class='/')
async def enter_void(request: Request):
    return templates.TemplateResponse('elementsmicrointeraction.html', {'request':request})

@app.get("/ghostserver", response_class='/')
async def enter_void(request: Request):
    return templates.TemplateResponse('myghost3.html', {'request':request})


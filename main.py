
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/lost-form", response_class=HTMLResponse)
async def lost_form(request: Request):
    return templates.TemplateResponse("lost.html", {"request": request})

@app.get("/found-form", response_class=HTMLResponse)
async def found_form(request: Request):
    return templates.TemplateResponse("found.html", {"request": request})

@app.get("/results", response_class=HTMLResponse)
async def results(request: Request):
    return templates.TemplateResponse("results.html", {"request": request})

from fastapi import FastAPI, Depends, Request, Form, status

from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from sqlalchemy.orm import Session

import model
from database import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html",
                                      {"request": request})
from fastapi import FastAPI, Depends, Request, Form, status

from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from sqlalchemy.orm import Session

import model
from database import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home(request: Request):
    #login = db.query(model.Login).all()
    return templates.TemplateResponse("index.html",
                                      {"request": request})

@app.post("/add")
def add(request: Request, address: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    new_login = model.Login(address=address, password=password)
    db.add(new_login)
    db.commit()

    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)

#0619 11.52完成
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
        yield db #定義生成器 使用 yield 將 db 作為生成器的產出值返回
    finally:
        db.close()
    
@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    todos = db.query(model.Todo).all()
    return templates.TemplateResponse("index.html",
                                      {"request": request, "todo_list": todos})

@app.post("/add")
def add(request: Request, title: str = Form(...), db: Session = Depends(get_db)):
    new_todo = model.Todo(title=title)
    db.add(new_todo)
    db.commit()

    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)

@app.get("/update/{todo_id}")
def update(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(model.Todo).filter(model.Todo.id == todo_id).first()
    todo.complete = not todo.complete
    db.commit()
 
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)

@app.get("/delete/{todo_id}")
def update(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(model.Todo).filter(model.Todo.id == todo_id).first()
    db.delete(todo)
    db.commit()
 
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)
 

from fastapi import FastAPI, Request, Depends, Form, responses, status
from fastapi.templating import Jinja2Templates
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import models
from database import engine, sessionlocal
from forms import UserCreateForm

templates = Jinja2Templates(directory="templates")
app = FastAPI()


def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()


models.Base.metadata.create_all(bind=engine)


@app.get('/')
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post('/register/')
async def register(request: Request, username: str = Form(...), email: str = Form(...), password: str = Form(...),
                   db: Session = Depends(get_db)):
    form = UserCreateForm(request)
    await form.load_data()
    print("submitted")
    if await form.is_valid():
        try:
            print(username)
            print(email)
            print(password)
            total_row = db.query(models.User).filter(models.User.email == email).first()
            print(total_row)
            if total_row == None:
                print("Save")
                users = models.User(username=username, email=email, password=password)
                db.add(users)
                db.commit()
                return responses.RedirectResponse("/", status_code=status.HTTP_302_FOUND)
            else:
                print("taken email")
                errors = ["The email has already taken"]
        except IntegrityError:
            return {"message": "Error"}

    else:
        print("Error Form")
        errors = form.errors
    return templates.TemplateResponse("index.html", {"request": request, "errors": errors})

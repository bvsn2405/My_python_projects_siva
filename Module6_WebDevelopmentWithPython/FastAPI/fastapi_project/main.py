from fastapi import FastAPI, Depends
import models
from config import settings
from db import engine, get_db
from hashing import Hasher
from models import Base, User
from schemas import UserCreate
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

tags = [
    {"name": "user",
     "description": "These are my user related routes"},
    {"name": "Products",
     "description": "These are my product related routes"}]

app = FastAPI(title=settings.title,
              description=settings.description,
              version=settings.version,
              contact={"Name": settings.name, "Email": settings.email},
              openapi_tags=tags)


@app.get('/users/', tags=["user"])
def get_user():
    return {"message": "Hello user"}


@app.get('/products/', tags=["Products"])
def get_product():
    return {"message": "Hello Product"}


@app.post('/users', tags=["user"], response_model=None)
def create_user(user: UserCreate, db1: Session = Depends(get_db)):
    user = User(email=user.email, password=Hasher.get_hash_password(user.password))
    db1.add(user)
    db1.commit()
    db1.refresh(user)
    return user

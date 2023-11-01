import os

from typing import Optional
from fastapi import FastAPI, Depends
from routes.test import router as test_router
from db.models.test_model import Users
from sqlalchemy.orm import Session
from db.connection import get_db


app = FastAPI()
app.include_router(test_router)


@app.get("/")
def index():
    return {"python": "Framework!"}


@app.get("/api-endpoint/{user_name}")
async def first_api(user_name):
    return {'message': user_name}


@app.get("/users/")
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(Users).offset(skip).limit(limit).all()
    return users

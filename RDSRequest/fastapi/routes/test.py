from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.connection import get_db
from crud import crud_test
from apis import test


router = APIRouter(
    prefix="/items"
)


@router.get("/test_route")
def test_index(db: Session = Depends(get_db)):
    res = test.test_index(db=db)
    return {"res": res}
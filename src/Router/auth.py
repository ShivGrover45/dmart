from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controller.auth import signup
from Db.database import get_db
from Schemas.schema import UserCreate

router=APIRouter()

@router.post('/signup')
def create_user(user:UserCreate,db:Session=Depends(get_db)):
    return  signup(user,db)

@router.post('/login')
def sign_in(user:UserCreate,db:Session=Depends(get_db)):
    pass

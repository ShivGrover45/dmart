from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controller.auth import signup,signin
from Db.database import get_db
from Schemas.schema import UserCreate,UserResponse,LoginRequest


router=APIRouter()

@router.post('/signup',response_model=UserResponse)
def create_user(user:UserCreate,db:Session=Depends(get_db)):
    return  signup(user,db)

@router.post('/login')
def sign_in(user:LoginRequest,db:Session=Depends(get_db)):
    return signin(user,db=db)

from sqlalchemy.orm import Session
from Db.models import User
from pwdlib import PasswordHash
from fastapi import HTTPException
from dotenv import load_dotenv
from datetime import datetime,timezone,timedelta
import jwt
import os 

load_dotenv()

jwt_secret=os.getenv("JWT_SECRET")

password_hash=PasswordHash.recommended()

def signup(user_data,db:Session):
    
    password=user_data.password
    hashed_password=password_hash.hash(password=password)
    user=User(
        username=user_data.username,
        hashed_password=hashed_password,
        role=user_data.role
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def signin(user_data,db:Session):
    username=user_data.username
    password=user_data.password
    user=db.query(User).filter(User.username==username).first()
    user_password=password_hash.verify(password=password,hash=user.hashed_password)
  
    if not user:
        raise HTTPException(status_code=401,detail="Invalid Username or Password")
    if not user_password:
        raise HTTPException(status_code=401,detail="Invalid username or password")
    payload={
        "id":user.id,
        "role":user.role,
        "exp":datetime.now(timezone.utc) + timedelta(hours=1)
    }
    encoded=jwt.encode(payload=payload,key=jwt_secret,algorithm="HS256")
    return {
        "access_token":encoded,
        "token_type":"bearer"
    }
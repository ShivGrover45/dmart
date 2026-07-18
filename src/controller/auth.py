from sqlalchemy.orm import Session
from Db.models import User
def signup(user_data,db:Session):
    user=User(
        username=user_data.username,
        hashed_password=user_data.password,
        role=user_data.role
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def signin(user_data,db:Session):
    
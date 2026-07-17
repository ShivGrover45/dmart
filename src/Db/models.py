from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import base

class User(base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,index=True,unique=True,nullable=False)
    password=Column(String,nullable=False)
    role=Column(String,nullable=False)

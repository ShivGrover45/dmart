from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime
from zoneinfo import ZoneInfo

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,index=True,unique=True,nullable=False)
    hashed_password=Column(String,nullable=False,name="password")
    role=Column(String,nullable=False)

class Product(Base):
    __tablename__="products"
    id=Column(Integer,primary_key=True)
    product_ref=Column(Integer,unique=True,nullable=False,index=True)
    name=Column(String,index=True,nullable=False)
    price=Column(Integer,nullable=False)
    stock=Column(Integer,nullable=False)
  
    purchase_items = relationship(
    "PurchaseItems",
    back_populates="product"
)

class Purchase(Base):
    __tablename__='purchases'
    id=Column(Integer,primary_key=True)
    total_amount=Column(Integer,nullable=False)
    created_at=Column(DateTime,default=lambda:datetime.now(ZoneInfo('Asia/Kolkata')),nullable=False)
    items = relationship("PurchaseItems", back_populates="purchase")

class PurchaseItems(Base):
    __tablename__='purchase_items'
    id=Column(Integer,primary_key=True)
    purchase_id=Column(Integer,ForeignKey('purchases.id'),nullable=False)
    product_id=Column(Integer,ForeignKey('products.id'),nullable=False)
    quantity=Column(Integer,nullable=False)
    price_at_purchase = Column(Integer, nullable=False)
    purchase = relationship("Purchase", back_populates="items")
    product = relationship("Product", back_populates="purchase_items")

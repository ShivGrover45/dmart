from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import List

class UserCreate(BaseModel):
    username: str
    password: str
    role: str


class UserResponse(BaseModel):
    id: int
    username: str
    role: str

    model_config = ConfigDict(from_attributes=True)



class ProductBase(BaseModel):
    product_ref: int
    name: str
    price: int
    stock: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: str | None = None
    price: int | None = None
    stock: int | None = None


class ProductResponse(ProductBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class PurchaseItemCreate(BaseModel):
    product_ref: int
    quantity: int


class PurchaseItemResponse(BaseModel):
    product_id: int
    quantity: int
    price_at_purchase: int

    model_config = ConfigDict(from_attributes=True)


class PurchaseCreate(BaseModel):
    items: List[PurchaseItemCreate]


class PurchaseResponse(BaseModel):
    id: int
    total_amount: int
    created_at: datetime
    items: List[PurchaseItemResponse]

    model_config = ConfigDict(from_attributes=True)
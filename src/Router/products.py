from fastapi import APIRouter,Depends
from Schemas.schema import ProductCreate,ProductBase,ProductResponse
from Db.database import get_db
from sqlalchemy.orm import Session
from controller.products import create_products

prod_router=APIRouter()

@prod_router.post('/add',response_model=ProductResponse)
def post_products(products:ProductCreate,db:Session=Depends(get_db)):
    return create_products(products,db)
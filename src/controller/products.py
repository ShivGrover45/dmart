from Db.models import Product
from sqlalchemy.orm import Session
from fastapi import HTTPException

def create_products(products,db:Session):
    prod_exist=db.query(Product).filter(Product.product_ref==products.product_ref).first()
    if not prod_exist:
       product=Product(
           product_ref=products.product_ref,
           name=products.name,
          price=products.price,
          stock=products.stock )
    else:
        raise HTTPException(status_code=409,detail="Product already exists")
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
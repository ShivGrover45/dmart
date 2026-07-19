
from dotenv import load_dotenv
from fastapi import HTTPException
import os
import jwt

load_dotenv()

jwt_secret=os.getenv("JWT_SECRET")
algorithm=os.getenv("ALGORITHM")

def verify_token(token):
    try:
        payload=jwt.decode(token,jwt_secret,algorithms=algorithm)
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401,detail="Token Expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401,detail="Invalid Token")
    return payload
    

def is_admin(payload):
    if(payload.get("role")=="admin"):
        return payload
    else:
        raise HTTPException(status_code=403,detail="Unauthorized Access")


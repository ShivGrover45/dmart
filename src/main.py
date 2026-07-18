from fastapi import FastAPI
from Db.database import Base
from Db.database import engine

from Router.auth import router

app=FastAPI(
    title="DMart API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(router=router,prefix='/auth',tags=['authentication'])

@app.get('/health')
def health_check():
    return {
        "status":"Healthy"
    }


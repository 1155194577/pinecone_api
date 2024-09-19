from fastapi import APIRouter
from app.db.config import pc
from app.util.load_abs_path import load_abs
load_abs()

indexes_api_router = APIRouter(prefix="/api/v1/indexes", tags=["indexes"])  

@indexes_api_router.get("/namespaces")
async def get_namespaces():
    print(pc.list_indexes())
    return {"test":"val"}  

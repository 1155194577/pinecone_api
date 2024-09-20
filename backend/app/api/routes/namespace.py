from fastapi import APIRouter,HTTPException
from app.util.load_abs_path import load_abs
from app.db.index_operation import delete_namespace
from fastapi.responses import JSONResponse  
from app.api.status import status_code
load_abs()

indexes_api_router = APIRouter(prefix="/api/v1/namespace/{namespace_name}", tags=["indexes"])  

@indexes_api_router.delete("/")
async def delete_namespace(namespace_name:str): 
    try:
        isSuccessfulDeletion = delete_namespace(namespace_name)
        return JSONResponse(status_code=status_code["success"],content={"isSuccessfulDeletion":isSuccessfulDeletion})
    except Exception as e:
        raise HTTPException(status_code=status_code["error"], detail=str(e))


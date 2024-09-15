from fastapi import FastAPI ,APIRouter,Query,HTTPException
# from fastapi.responses import JSONResponse
from app.api.status import status_code,status_message   
from app.util.load_abs_path import load_abs
from app.db.db_operation import get_vectors
from app.db.config import NAMESPACE_NAME
# from fastapi.encoders import jsonable_encoder
# import json
from app.base_models.db_base_models import Vector
load_abs()

vector_api_router = APIRouter(prefix="/api/v1/vectors", tags=["vectors"])  

@vector_api_router.get("/",response_model=Vector)
async def get_vector(vector_id:str = Query(None)):
    try:
        if vector_id is None:
            raise HTTPException(status_code=status_code["invalid_vector_id"], detail=status_message["invalid_vector_id"])
        else:
            res_vector = get_vectors(NAMESPACE_NAME,[vector_id])
            return res_vector[vector_id]
    except Exception as e:
            raise HTTPException(status_code=status_code["error"], detail=str(e))
    


from fastapi import FastAPI ,APIRouter,Query,HTTPException
from fastapi.responses import JSONResponse
from app.api.status import status_code,status_message,VectorCreationError,VectorLengthError,InvalidVectorIdError
from app.util.load_abs_path import load_abs
from app.db.db_operation import get_vectors,add_vectors,del_vectors,vector_exist
from app.db.config import NAMESPACE_NAME,PINECONE_DIMENSION
from app.base_models.db_base_models import Vector
load_abs()

vector_api_router = APIRouter(prefix="/api/v1/vector", tags=["vector"])  

@vector_api_router.get("/",response_model=Vector)
async def get_vector(vector_id:str = Query(None)):
    try:
        if len(vector_id) == 0: 
            raise InvalidVectorIdError(user_input=vector_id)
        else:
            res_vector = get_vectors(NAMESPACE_NAME,[vector_id])
            if (not res_vector):
                raise InvalidVectorIdError(user_input=vector_id)
            return res_vector[vector_id]
    except Exception as e:
            raise HTTPException(status_code=status_code["error"], detail=str(e))
    
@vector_api_router.post("/")
async def create_vector(vector:Vector):
    try:
        vector_dimension = len(vector.values)
        if vector_dimension != PINECONE_DIMENSION:
            raise VectorLengthError()
        isSuccessfulCreation = add_vectors(NAMESPACE_NAME,[vector])
        if (not isSuccessfulCreation):
            raise VectorCreationError()
        return JSONResponse(status_code=status_code["success"],content={"isSuccessfulCreation":isSuccessfulCreation})
    except Exception as e:
        raise HTTPException(status_code=status_code["error"], detail=str(e))
    
@vector_api_router.delete("/")
async def delete_vector(vector_id:str = Query(None)): 
    try:
        if len(vector_id) == 0 or not vector_exist(NAMESPACE_NAME,vector_id):
            raise InvalidVectorIdError(user_input=vector_id) 
        isSuccessfulDeletion = del_vectors(NAMESPACE_NAME,[vector_id])
        return JSONResponse(status_code=status_code["success"],content={"isSuccessfulDeletion":isSuccessfulDeletion})
    except Exception as e:
        raise HTTPException(status_code=status_code["error"], detail=str(e))  
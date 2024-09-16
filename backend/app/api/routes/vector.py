from fastapi import APIRouter,Query,HTTPException
from fastapi.responses import JSONResponse
from app.api.status import status_code,VectorCreationError,VectorLengthError,InvalidVectorIdError,InvalidTopKError
from app.util.load_abs_path import load_abs
from app.db.db_operation import get_vectors,add_vectors,del_vectors,vector_exist,search_vectors
from app.db.config import NAMESPACE_NAME,PINECONE_DIMENSION
from app.base_models.db_base_models import Vector,VectorSearchQuery
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
        vector_id = vector.id 
        if len(vector_id) == 0:
            raise InvalidVectorIdError(user_input=vector_id)
        if vector_exist(NAMESPACE_NAME,vector_id):
            raise VectorCreationError(message=f"Vector with id {vector_id} already exists")
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

@vector_api_router.post("/search")   
async def search_vector(query:VectorSearchQuery):
    try:
        vector_value = query.values
        vector_dimension = len(vector_value)
        top_k = query.top_k
        include_metadata = query.include_metadata
        include_values = query.include_values
        if vector_dimension != PINECONE_DIMENSION:
            raise VectorLengthError()
        if top_k <= 0:
            raise InvalidTopKError() 
        search_results = search_vectors(NAMESPACE_NAME,vector_value,top_k,include_values,include_metadata)
        query_response = search_results.to_dict()
        return JSONResponse(status_code=status_code["success"], content=query_response)
    except Exception as e:
        raise HTTPException(status_code=status_code["error"], detail=str(e))
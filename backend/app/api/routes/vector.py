from fastapi import APIRouter,Query,HTTPException
from fastapi.responses import JSONResponse
from app.api.status import status_code,VectorCreationError,VectorLengthError,InvalidVectorIdError,InvalidTopKError,InvalidIndexNameError,InvalidNamespaceNameError
from app.util.load_abs_path import load_abs
from app.db.db_operation import get_vectors,add_vectors,del_vectors,vector_exist,search_vectors 
from app.db.index_operation import get_dimension,get_index_by_index_name
from app.base_models.db_base_models import Vector,VectorSearchQuery,VectorIdList
from app.util.rules import is_valid_index_name,is_valid_namespace_name
from typing import List

load_abs()

vector_api_router = APIRouter(prefix="/api/v1/vector/{index_name}/{namespace_name}", tags=["vector"])  


@vector_api_router.get("/",response_model=Vector)
async def get_vector(index_name:str,namespace_name:str,vector_id:str = Query(None)):
    try:
        if len(vector_id) == 0: 
            raise InvalidVectorIdError(user_input=vector_id)
        if not is_valid_index_name(index_name):
            raise InvalidIndexNameError(user_input=index_name)
        if not is_valid_namespace_name(namespace_name):
            raise InvalidNamespaceNameError(user_input=namespace_name)
        else:
            res_vector = get_vectors(index_name,namespace_name,[vector_id])
            if (not res_vector):
                raise InvalidVectorIdError(user_input=vector_id)
            print(res_vector)
            return res_vector[vector_id]
    except Exception as e:
            raise HTTPException(status_code=status_code["error"], detail=str(e))
    
@vector_api_router.post("/")
async def create_vector(index_name:str,namespace_name:str,vector:Vector):
    try:
        vector_id = vector.id 
        if len(vector_id) == 0:
            raise InvalidVectorIdError(user_input=vector_id)
        if vector_exist(index_name,namespace_name,vector_id):
            raise VectorCreationError(message=f"Vector with id {vector_id} already exists")
        vector_dimension = len(vector.values)
        if vector_dimension != get_dimension(index_name): 
            raise VectorLengthError()
        isSuccessfulCreation = add_vectors(index_name,namespace_name,[vector])
        if (not isSuccessfulCreation):
            raise VectorCreationError()
        return JSONResponse(status_code=status_code["success"],content={"isSuccessfulCreation":isSuccessfulCreation})
    except Exception as e:
        raise HTTPException(status_code=status_code["error"], detail=str(e))

@vector_api_router.delete("/")
async def delete_vector(index_name:str,namespace_name:str,vector_id:str = Query(None)): 
    try:
        if len(vector_id) == 0 or not vector_exist(index_name,namespace_name,vector_id):
            raise InvalidVectorIdError(user_input=vector_id) 
        isSuccessfulDeletion = del_vectors(index_name,namespace_name,[vector_id])
        return JSONResponse(status_code=status_code["success"],content={"isSuccessfulDeletion":isSuccessfulDeletion})
    except Exception as e:
        raise HTTPException(status_code=status_code["error"], detail=str(e))  

@vector_api_router.post("/search")   
async def search_vector(index_name:str,namespace_name:str,query:VectorSearchQuery):
    try:
        vector_value = query.values
        vector_dimension = len(vector_value)
        top_k = query.top_k
        include_metadata = query.include_metadata
        include_values = query.include_values
        if vector_dimension != get_dimension(index_name): 
            raise VectorLengthError()
        if top_k <= 0:
            raise InvalidTopKError() 
        search_results = search_vectors(index_name,namespace_name,vector_value,top_k,include_values,include_metadata)
        query_response = search_results.to_dict()
        return JSONResponse(status_code=status_code["success"], content=query_response)
    except Exception as e:
        raise HTTPException(status_code=status_code["error"], detail=str(e))
    
@vector_api_router.get("/list",response_model=VectorIdList)
async def get_vector_list_paginated(index_name:str,namespace_name:str,page_token:str = Query(None),limit:int = Query(10)):
    try:
        print("namespace,page_token,limit",namespace_name,page_token,limit)  
        index = get_index_by_index_name(index_name)
        results = index.list_paginated(
        namespace=namespace_name,
        pagination_token=page_token,
        limit=limit)
        vector_ids = [x["id"] for x in results["vectors"]]
        token = results.get("pagination",{}).get("next",None)
        print(vector_ids,token)
        vector_id_list = VectorIdList(ids=vector_ids,page_token=token,limit=limit)
        return vector_id_list
    except Exception as e:
        raise HTTPException(status_code=status_code["error"], detail=str(e))


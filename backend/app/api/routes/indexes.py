from fastapi import APIRouter,HTTPException
# from app.db.config import pc,create_index,delete_index
from app.util.load_abs_path import load_abs
from app.db.index_operation import get_all_namespaces_name,get_all_indexes_name,get_namespace_stats,create_index,delete_index
from app.api.status import status_code,status_message
from fastapi.responses import JSONResponse
from app.base_models.db_base_models import IndexStats,PineConeIndex
from app.util.helper import get_keys_from_dict
from app.api.status import InvalidIndexNameError
from app.util.rules import is_valid_index_name
load_abs()

indexes_api_router = APIRouter(prefix="/api/v1/indexes", tags=["indexes"])  

@indexes_api_router.get("/")
async def get_all_indexes():
    try:
        indexes = get_all_indexes_name()
        return JSONResponse(status_code=status_code["success"],content={"indexes":indexes})
    except Exception as e:
        raise HTTPException(status_code=status_code["error"], detail=str(e))    

# @indexes_api_router.get("/{index_name}/namespaces")
# async def get_all_namespaces(index_name:str):
#     try:
#         namespaces = get_all_namespaces_name(index_name)
#         return JSONResponse(status_code=status_code["success"],content={"namespaces":namespaces})
#     except Exception as e:
#         raise HTTPException(status_code=status_code["error"], detail=str(e))    

@indexes_api_router.get("/{index_name}/stats",response_model=IndexStats)   
async def get_statistic_of_index(index_name:str):
    try:
        stats = get_namespace_stats(index_name)
        # assert  stats is not None
        keys = get_keys_from_dict(stats["namespaces"])
        stat_response = IndexStats(dimension=stats["dimension"],index_fullness=stats["index_fullness"],namespaces=keys,total_vector_count=stats["total_vector_count"])
        # assert stat_response is not None
        return stat_response
    except Exception as e:
        raise HTTPException(status_code=status_code["error"], detail=str(e))
    
@indexes_api_router.post("/")
async def create_index_in_db(pinecone_index: PineConeIndex):  
    try:
        index_name = create_index(pinecone_index)
        assert index_name is not None
        return JSONResponse(status_code=status_code["success"], content={"message": status_message["index_creation_successful"]})
    except Exception as e:
        raise HTTPException(status_code=status_code["error"], detail=str(e))
    
@indexes_api_router.delete("/{index_name}")
async def delete_index_in_db(index_name:str): 
    try:
        if not is_valid_index_name(index_name):
            raise InvalidIndexNameError(user_input=index_name)
        isSuccessfulDeletion = delete_index(index_name)
        return JSONResponse(status_code=status_code["success"],content={"isSuccessfulDeletion":isSuccessfulDeletion})
    except Exception as e:
        raise HTTPException(status_code=status_code["error"], detail=str(e))
    

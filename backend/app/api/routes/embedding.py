from fastapi import APIRouter,HTTPException,UploadFile,File
from fastapi.responses import JSONResponse
from app.api.status import status_code,status_message
from pydantic import BaseModel
from typing import List
embedding_api_router = APIRouter(prefix="/api/v1/embedding", tags=["embedding"])  
class EmbeddingResponse(BaseModel):
    embedding: List[int]

@embedding_api_router.post("/", response_model=EmbeddingResponse)
async def convert_music_to_vector(file: UploadFile = File(...)):
    try:
        return EmbeddingResponse(embedding=[1, 2, 3, 3,9,3])
    except Exception as e:
        raise HTTPException(status_code=status_code["error"], detail=str(e))
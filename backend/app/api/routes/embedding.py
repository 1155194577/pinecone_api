from fastapi import APIRouter,HTTPException,UploadFile,File
from fastapi.responses import JSONResponse
from app.api.status import status_code,status_message
from pydantic import BaseModel
from typing import List
import os
import librosa
from app.api.embedder import MusicEmbedder,Music
embedding_api_router = APIRouter(prefix="/api/v1/embedding", tags=["embedding"])  


class EmbeddingResponse(BaseModel):
    embedding: list[float]

    
@embedding_api_router.post("/", response_model=EmbeddingResponse)
async def convert_music_to_vector(file: UploadFile = File(...)):
    music_path = f"{file.filename}"  # Temporary path for the uploaded file
    try:
        curr_dir = os.getcwd()
        full_file_path = os.path.join(curr_dir,music_path)
        contents = await file.read()
        with open(full_file_path, "wb") as f:
            f.write(contents)
        print(librosa.__version__,full_file_path)

        # Load the audio file using librosa
        print("ddd")
        y, sr = librosa.load(full_file_path, sr=None)
    

        # Create a Music instance (assuming Music is defined elsewhere)
        query = Music(y=y, sr=sr, music_name=file.filename, audio_url=None)  # Replace None with actual S3 URL if needed
        query.compute_music_features()
        print(query)
        ##query_vector = MusicEmbedder.convert_music_to_vector(query)
        ##print(query_vector)
        demo_vector= [1,2,3,4,5,6] 
        return EmbeddingResponse(embedding=demo_vector)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        # Clean up the temporary audio file
        if os.path.exists(music_path):
            os.remove(music_path)  # Remove the file if it exists

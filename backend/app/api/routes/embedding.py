from fastapi import APIRouter,HTTPException,UploadFile,File
from fastapi.responses import JSONResponse
from app.api.status import status_code,status_message
from pydantic import BaseModel
from typing import List
from pydub import AudioSegment
import os
import librosa
from app.api.embedder import MusicEmbedder,Music
embedding_api_router = APIRouter(prefix="/api/v1/embedding", tags=["embedding"])  


class EmbeddingResponse(BaseModel):
    embedding: list[float]

def trim_audio(file_path, duration):
    """Trim the audio file to the first 'duration' seconds."""
    # Load the audio file
    print("a")
    audio = AudioSegment.from_file(file_path)

    # Trim to the first 'duration' seconds
    trimmed_audio = audio[:duration * 1000]  # duration in milliseconds
    print("b")
    # Export the trimmed audio
    # trimmed_file_path = file_path.replace(".m4a", ".mp3")
    trimmed_audio.export(file_path, format="mp3")

    print(f"Trimmed audio saved to: {file_path}")
    return file_path
    
@embedding_api_router.post("/", response_model=EmbeddingResponse)
async def convert_music_to_vector(file: UploadFile = File(...)):
    music_path = f"{file.filename}"  # Temporary path for the uploaded file
    try:
        curr_dir = os.getcwd()
        full_file_path = os.path.join(curr_dir,music_path)
        contents = await file.read()
        with open(full_file_path, "wb") as f:
            f.write(contents)
        trimmed_file_path = trim_audio(full_file_path,30)
        print(librosa.__version__, trimmed_file_path)
        
        # Load the audio file using librosa
        y, sr = librosa.load(trimmed_file_path, sr=None)
        # Create a Music instance (assuming Music is defined elsewhere)
        query = Music(y=y, sr=sr, music_name=file.filename, audio_url=None)  # Replace None with actual S3 URL if needed
        query.compute_music_features()
        print(query)
        min_map = {'tempo': 51.6796875, 'stability_score': 0.00021142619917965743, 'beat_strength_score': 1.7689238, 'dynamic_range': 0.028075214, 'mean_rmse': 0.0080167325, 'mean_spectral_centroid': 724.0536236293076}
        max_map = {'tempo': 184.5703125, 'stability_score': 0.0005543932024575787, 'beat_strength_score': 9.631109, 'dynamic_range': 0.66027665, 'mean_rmse': 0.31266674, 'mean_spectral_centroid': 3587.1374576583225}
        embedder1 = MusicEmbedder(min_map,max_map)
        query_vector = embedder1.convert_music_to_vector(query)
        print(query_vector)
        return EmbeddingResponse(embedding=query_vector)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        # Clean up the temporary audio file
        if os.path.exists(music_path):
            os.remove(music_path)  # Remove the file if it exists

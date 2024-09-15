from app.api.api import app
import uvicorn
from dotenv import load_dotenv
import os
load_dotenv()
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT")) or 8000,reload=True)
    print("Server is running on port: ",os.getenv("PORT"))
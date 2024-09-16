from fastapi import FastAPI
from app.api.routes.vector import vector_api_router

app = FastAPI()
app.include_router(vector_api_router)

from fastapi import FastAPI
from app.api.routes.vector import vector_api_router
from app.api.routes.indexes import indexes_api_router   
from app.api.routes.aws import aws_api_router
from app.api.routes.embedding import embedding_api_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(vector_api_router)
app.include_router(indexes_api_router)
app.include_router(aws_api_router)
app.include_router(embedding_api_router)    
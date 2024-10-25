from fastapi import FastAPI
from app.api.routes.vector import vector_api_router
from app.api.routes.indexes import indexes_api_router   
from app.api.routes.aws import aws_api_router
app = FastAPI()
app.include_router(vector_api_router)
app.include_router(indexes_api_router)
app.include_router(aws_api_router)
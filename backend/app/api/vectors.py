from fastapi import FastAPI ,APIRouter
app = FastAPI()

api_router = APIRouter(prefix="/api/v1/vectors", tags=["vectors"])  

# Define a route in the router
@api_router.get("/hello")
async def hello():
    return {"message": "Hello, World!"}

# Include the router in the main application
app.include_router(api_router)

from app.db.config import PINECONE_DIMENSION
status_code = {
    "success": 200,
    "invalid_vector_id": 400,
    "invalid_vector_length": 400,
    "error": 500,
    "invalid_vector_creation": 500, 
}

status_message = { 
    "invalid_vector_id": "Invalid vector id",
    "invalid_vector_length": f"{PINECONE_DIMENSION} dimensions are required for a vector",
    "invalid_vector_creation": "Invalid vector creation",  
}

class VectorCreationError(Exception):
    def __init__(self, message=status_message["invalid_vector_creation"], status_code=status_code["invalid_vector_creation"]):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} (status code: {self.status_code})"

class VectorLengthError(Exception):
    def __init__(self, message=status_message["invalid_vector_length"], status_code=status_code["invalid_vector_length"]):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} (status code: {self.status_code})"
from app.db.config import PINECONE_DIMENSION
status_code = {
    "success": 200,
    "invalid_vector_id": 404,
    "invalid_vector_length": 400,
    "error": 500,
    "invalid_vector_creation": 500, 
    "invalid_vector_deletion": 500, 
    "invalid_top_k": 400,
    "invalid_index_name": 400,
    "invalid_namespace_name": 400,
}

status_message = { 
    "invalid_vector_id": "Invalid vector id",
    "invalid_vector_length": f"{PINECONE_DIMENSION} dimensions are required for a vector",
    "invalid_vector_creation": "Invalid vector creation",  
    "invalid_vector_deletion": "Invalid vector deletion",
    "invalid_top_k": "Top k value should be greater than 0",
    "invalid_index_name": "Invalid index name",
    "invalid_namespace_name": "Invalid namespace name",
    "index_creation_successful": "Index creation successful",
    "file_upload_successful": "File upload successful"
}
class InvalidIndexNameError(Exception):
    def __init__(self, message=status_message["invalid_index_name"], status_code=status_code["invalid_index_name"], user_input=None):
        self.message = message
        self.status_code = status_code
        self.user_input = user_input
        super().__init__(self.message)
    
    def __str__(self):
        return "Invalid Index Name" 
class InvalidNamespaceNameError(Exception):
    def __init__(self, message=status_message["invalid_namespace_name"], status_code=status_code["invalid_namespace_name"], user_input=None):
        self.message = message
        self.status_code = status_code
        self.user_input = user_input
        super().__init__(self.message)
    
    def __str__(self):
       return "Invalid Namespace Name" 
class VectorDeletionError(Exception):
    def __init__(self, message=status_message["invalid_vector_deletion"], status_code=status_code["invalid_vector_deletion"]):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)
    
    def __str__(self):
        return "Vector Deletion Error"
class VectorCreationError(Exception):
    def __init__(self, message=status_message["invalid_vector_creation"], status_code=status_code["invalid_vector_creation"]):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

    def __str__(self):
        return "vector creation error"

class VectorLengthError(Exception):
    def __init__(self, message=status_message["invalid_vector_length"], status_code=status_code["invalid_vector_length"]):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

    def __str__(self):
        return "vector length error"

class InvalidVectorIdError(Exception):
    def __init__(self, message=status_message["invalid_vector_id"], status_code=status_code["invalid_vector_id"],user_input=None):
        self.message = message
        self.status_code = status_code
        self.user_input = user_input
        super().__init__(self.message)
    
    def __str__(self):
        return "invalid vector Id error"

class InvalidTopKError(Exception):
    def __init__(self, message=status_message["invalid_top_k"], status_code=status_code["invalid_top_k"]):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

    def __str__(self):
         return "invalid Top k"

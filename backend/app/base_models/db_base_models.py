from pydantic import BaseModel
from typing import Optional,List
class VectorSearchQuery(BaseModel):
    values: List[float]
    top_k: int
    include_metadata: Optional[bool] = False
    include_values: Optional[bool] = False

class Vector(BaseModel):
    id: str
    values: List[float]
    metadata: dict

class VectorArray(BaseModel):
    vectors: List[Vector]

class VectorSearchResult(BaseModel):
    id: str
    score: float
    values: List[float]

class VectorSearchResultArray(BaseModel):
     matches:list

class PineConeIndex(BaseModel):
    name : str 
    dimension: int
    metric: str 
    cloud : str 
    region : str

class IndexStats(BaseModel):
    dimension: int
    index_fullness: float
    namespaces: List[str]
    total_vector_count: int

class VectorIdList(BaseModel):
        ids: List[str]
        page_token: Optional[str] = None
        limit: int  

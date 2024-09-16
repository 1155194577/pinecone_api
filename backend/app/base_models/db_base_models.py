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

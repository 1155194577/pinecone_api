from pydantic import BaseModel

class Vector(BaseModel):
    id: str
    values: list[float]
    metadata: dict
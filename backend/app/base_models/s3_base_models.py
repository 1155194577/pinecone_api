from pydantic import BaseModel
from typing import List
class S3UrlData(BaseModel):
    s3_url: str
    file_name: str
class S3UrlArrayReponse(BaseModel):
    data: List[S3UrlData]
from fastapi import APIRouter,UploadFile,File,HTTPException
import boto3
from app.util.load_abs_path import load_abs
from app.api.status import status_code
from fastapi.responses import JSONResponse
from app.base_models.s3_base_models import S3UrlData,S3UrlArrayReponse
from app.api.status import status_message,status_code
from typing import Optional
aws_api_router = APIRouter(prefix="/api/v1/s3/{bucket_name}", tags=["aws"])  
load_abs()
s3_client = boto3.client('s3')

def list_files_in_bucket(bucket_name):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            return [obj['Key'] for obj in response['Contents']]
        else:
            return []
    except Exception as e:
        print(f"Error fetching files: {e}")
        return []
def create_presigned_url(bucket_name, file_name, expiration=31536000):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url('get_object',
            Params={'Bucket': bucket_name, 'Key': file_name},
            ExpiresIn=expiration)
    except Exception as e:
        print(e)
        return None
    return response
@aws_api_router.get("/file",response_model=S3UrlArrayReponse)
async def get_file_url_from_s3(bucket_name: str, file_name: Optional[str] = None):
    try:
        s3url_data_arr = []
        if (file_name is None):
            file_names = list_files_in_bucket(bucket_name)
            for file_name in file_names:
                url = create_presigned_url(bucket_name, file_name)
                s3_url_data = S3UrlData(s3_url=url,file_name=file_name)
                s3url_data_arr.append(s3_url_data)
        else: 
            url = create_presigned_url(bucket_name, file_name)
            s3_url_data = S3UrlData(s3_url=url,file_name=file_name)
            s3url_data_arr.append(s3_url_data)
        return S3UrlArrayReponse(data=s3url_data_arr)
    except Exception as e:
        raise HTTPException(status_code=status_code["error"], detail=str(e))


@aws_api_router.post("/file")
async def upload_file_to_s3(bucket_name:str, file: UploadFile = File(...)):
        try:
            s3_client.upload_fileobj(file.file, bucket_name, file.filename)
            return JSONResponse(status_code=status_code["success"], content={"message": status_message["file_upload_successful"]})
        except Exception as e:
            raise HTTPException(status_code=status_code["error"], detail=str(e))
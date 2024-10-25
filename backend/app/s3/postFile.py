import boto3 

def post_file_from_s3(local_dir, bucket_name, object_name):
    s3 = boto3.client('s3')
    s3.upload_file('test.txt', 'aist2010', 'abc.txt')
    return "HelloWorld"

def get_file_from_s3(local_dir, bucket_name, object_name):
    s3 = boto3.client('s3')
    s3.download_file('aist2010', 'abc.txt', 'test.txt')
    return "HelloWorld"

if __name__ == "__main__":
    print(get_file())
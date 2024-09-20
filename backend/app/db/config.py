import os
from dotenv import load_dotenv
from pinecone import Pinecone,ServerlessSpec
# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Pinecone configuration (sample)
PINECONE_API_KEY = os.environ.get("PINE_CONE_KEY")
PINECONE_DIMENSION = 8
PINECONE_METRIC = "cosine"
PINECONE_CLOUD = "aws"
PINECONE_REGION = "us-east-1"
pc = Pinecone(api_key=PINECONE_API_KEY)
INDEX_NAME = "quickstart"
NAMESPACE_NAME = "ns1"

def create_new_index(index_name):
    index_names = [index.name for index in pc.list_indexes()]
    try:
        if index_name in index_names:
            print("Index already exists")
            index = pc.Index(index_name)
            return index
        else:
            pc.create_index(
                name=index_name,
                dimension=PINECONE_DIMENSION, 
                metric=PINECONE_METRIC, 
                spec=ServerlessSpec(
                    cloud=PINECONE_CLOUD,
                    region=PINECONE_REGION
                )) 
            index = pc.Index(index_name)
            return index
    except Exception as e:
        print(str(e))
        return None

def echo(a):
    return a
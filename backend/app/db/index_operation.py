from app.db.config import pc
from app.base_models.db_base_models import PineConeIndex
from pinecone import ServerlessSpec
from app.util.rules import is_valid_index_name

def get_dimension(index_name):
    index = get_index_by_index_name(index_name)
    stats = index.describe_index_stats()
    dimension = stats["dimension"]
    return dimension

def get_index_by_index_name(index_name):  
    ## only use this function if you are sure that the index exists 
    try:
        if not is_valid_index_name(index_name):
            print("Invalid index name")
            return None
        index = pc.Index(index_name)
        return index
    except Exception as e:
        print(str(e))
        return None
    
def create_index(pinecone_index: PineConeIndex):
    index_names = [index.name for index in pc.list_indexes()]
    index_name = pinecone_index.name
    index_dimension = pinecone_index.dimension 
    index_metric = pinecone_index.metric 
    index_cloud = pinecone_index.cloud
    index_region = pinecone_index.region
    try:
        if index_name in index_names:
            print("Index already exists")
            index = pc.Index(index_name)
            return index
        else:
            pc.create_index(
                name=index_name,
                dimension=index_dimension, 
                metric=index_metric, 
                spec=ServerlessSpec(
                    cloud=index_cloud,
                    region=index_region, 
                )) 
            index = pc.Index(index_name)
            return index
    except Exception as e:
        print(str(e))
        return None

def delete_index(index_name):
    try:
        pc.delete_index(index_name)
        return True
    except Exception as e:
        print(str(e))
        return False

def get_all_indexes_name():
    indexes = pc.list_indexes()
    indexes_name = [index["name"] for index in indexes]
    print(indexes_name)
    return indexes_name

def get_all_namespaces_name(index_name):
    index = pc.Index(index_name)
    stats = index.describe_index_stats()
    arr = stats["namespaces"]
    keys = [key for key in arr]
    return keys
          
def get_namespace_stats(index_name,namespace_name):
    index = pc.Index(index_name)
    stats = index.describe_index_stats()
    arr = stats["namespaces"]
    keys = [key for key in arr]
    if namespace_name in keys:
        return arr[namespace_name]
    else:
        return None
    
def delete_namespace(index_name,namespace_name):
    try:
        index = pc.Index(index_name)
        index.delete(namespace=namespace_name, delete_all=True)
        return True
    except Exception as e:
        print(str(e))
        return False
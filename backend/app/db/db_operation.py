from .config import INDEX_NAME,create_new_index,NAMESPACE_NAME
from typing import List
from .base_models import Vector
index = create_new_index(INDEX_NAME)

def add_vectors(namespace_name:str,vectors_arr: List[Vector]):
    print("Namespace:", namespace_name)
    print("Vectors:", vectors_arr)
    if namespace_name == "":
        print("Namespace name is empty")
        return False
    if len(vectors_arr) == 0:
        print("Vector list is empty")
        return False
    try:
        index.upsert(
        vectors=[
            {
                "id": vec.id, 
                "values": vec.values, 
                "metadata": vec.metadata
            } for vec in vectors_arr
        ],
        namespace= namespace_name
        )
        print("Successful, Number of vectors added: ",len(vectors_arr))
        return True
    except Exception as e:
        print("Error in adding vectors :",str(e))
        return False
    
def del_vectors(namespace_name:str,vectors_id_arr:List[str]):
    if namespace_name == "":
        print("Namespace name is empty")
        return False
    if len(vectors_id_arr) == 0:
        print("Vector list is empty")
        return False
    try:    
            index.delete(ids=vectors_id_arr, namespace=namespace_name)
            print("Successful, Number of vectors deleted: ",len(vectors_id_arr))
            return True
    except Exception as e:  
        print("Error in deleting vectors",str(e))
        return False

def get_vectors(namespace_name:str,vectors_id_arr:List[str]):
    if namespace_name == "":
        print("Namespace name is empty")
        return False
    if len(vectors_id_arr) == 0:
        print("Vector list is empty")
        return False
    try:
        res = index.fetch(ids=vectors_id_arr, namespace=namespace_name)
        vectors = res.vectors
        print("Successful, Number of vectors fetched: ",len(vectors))
        return vectors
    except Exception as e:
        print("Error in fetching vectors",str(e))
        return False
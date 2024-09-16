from .config import INDEX_NAME,create_new_index,NAMESPACE_NAME
from typing import List
from ..base_models.db_base_models import Vector
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
        print("Successful, Number of vectors fetched: ",len(vectors),type(vectors))
        return vectors
    except Exception as e:
        print("Error in fetching vectors",str(e))
        return False
    
def search_vectors(namespace_name: str, query_vector: Vector, top_k: int,allow_values: bool = False, allow_metadata: bool = False):
    if namespace_name == "":
        print("Namespace name is empty")
        return False
    if top_k <= 0:
        print("Top k must be greater than 0")
        return False
    # print(query_vector.values)
    try:
        res = index.query(
            vector=[[0.1]*8],
            top_k=top_k,
            namespace=namespace_name,
            include_values=allow_values, 
            include_metadata=allow_metadata
        )
        return res
    except Exception as e:
        print("Error in searching vectors", str(e))
        return False
    
def vector_exist(namespace_name: str, vector_id: str):
    try:
        vectors = get_vectors(namespace_name, [vector_id])
        return True if vector_id in vectors else False
    except Exception as e:
        print("Error in checking vector existence", str(e))
        return False
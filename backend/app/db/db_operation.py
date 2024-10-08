from app.db.index_operation import get_index_by_index_name
from typing import List
from app.base_models.db_base_models import Vector

def add_vectors(index_name: str, namespace_name: str, vectors_arr: List[Vector]):
    index = get_index_by_index_name(index_name)
    print("index name:", index_name)
    print("Namespace:", namespace_name)
    print("Vectors:", vectors_arr)
    if namespace_name == "": 
        print("Namespace name is empty")
        return False
    if index_name == "":
        print("Index name is empty")
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
            namespace=namespace_name
        )
        print("Successful, Number of vectors added: ", len(vectors_arr))
        return True
    except Exception as e:
        print("Error in adding vectors :", str(e))
        return False


def del_vectors(index_name: str, namespace_name: str, vectors_id_arr: List[str]):
    index = get_index_by_index_name(index_name)
    if namespace_name == "":
        print("Namespace name is empty")
        return False
    if index_name == "":
        print("Index name is empty")
        return False
    if len(vectors_id_arr) == 0:
        print("Vector list is empty")
        return False
    try:
        index.delete(ids=vectors_id_arr, namespace=namespace_name)
        print("Successful, Number of vectors deleted: ", len(vectors_id_arr))
        return True
    except Exception as e:
        print("Error in deleting vectors", str(e))
        return False


def get_vectors(index_name: str, namespace_name: str, vectors_id_arr: List[str]):
    index = get_index_by_index_name(index_name)
    if namespace_name == "":
        print("Namespace name is empty")
        return False
    if len(vectors_id_arr) == 0:
        print("Vector list is empty")
        return False
    try:
        res = index.fetch(ids=vectors_id_arr, namespace=namespace_name)
        vectors = res.vectors
        print("Successful, Number of vectors fetched: ", len(vectors), type(vectors))
        return vectors
    except Exception as e:
        print("Error in fetching vectors", str(e))
        return False

def get_all_vectors_id(index_name: str, namespace_name: str,vector_dimension:int):
    index = get_index_by_index_name(index_name)
    random_vector = [1.0]*vector_dimension
    res = search_vectors(index_name, namespace_name, random_vector, vector_dimension, allow_values=False, allow_metadata=False)
    print(res)
    return res 
def search_vectors(index_name: str, namespace_name: str, query_vector: List[float], top_k: int,
                   allow_values: bool = False, allow_metadata: bool = False):
    index = get_index_by_index_name(index_name)
    if namespace_name == "":
        print("Namespace name is empty")
        return False
    if index_name == "":
        print("Index name is empty")
        return False
    if top_k <= 0:
        print("Top k must be greater than 0")
        return False
    try:
        res = index.query(
            vector=query_vector,
            top_k=top_k,
            namespace=namespace_name,
            include_values=allow_values,
            include_metadata=allow_metadata
        )
        return res
    except Exception as e:
        print("Error in searching vectors", str(e))
        return False


def vector_exist(index_name: str, namespace_name: str, vector_id: str):
    try:
        vectors = get_vectors(index_name, namespace_name, [vector_id])
        return True if vector_id in vectors else False
    except Exception as e:
        print("Error in checking vector existence", str(e))
        return False

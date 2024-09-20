from app.db.index_operation import get_all_indexes_name, get_all_namespaces_name, get_namespace_stats,create_index,is_valid_index_name
from app.base_models.db_base_models import PineConeIndex   
import pytest 
from app.db.index_operation import get_all_indexes_name, get_all_namespaces_name, get_namespace_stats, create_index, is_valid_index_name, delete_index, delete_namespace
def main_create_index():
    pinecone_index = PineConeIndex(name="test-index",dimension=8,metric="cosine",cloud="aws",region="us-east-1")
    res = create_index(pinecone_index)
    assert res is not None 

@pytest.mark.parametrize("index_name", [
    ("test-index"),
    ("test-index-1"),
    ("test-index-2"),
    ("test-index-3"),
    ("test-index-4"),
    ("test-index-5"),
    ("test-index-6"),
    ("test-index-7"),
    ("test-index-8"),
    ("test-index-9"),
])
def test_is_valid_index_name(index_name):
    res = is_valid_index_name(index_name)
    assert res == True

def test_get_all_indexes_name():
    res = get_all_indexes_name()
    assert len(res) > 0 

def test_get_all_namespaces_name():
    res = get_all_namespaces_name("test-index")
    assert len(res) > 0 

def test_get_namespace_stats():
    res = get_namespace_stats("test-index", "test_namespace")
    assert res is not None

def test_create_index():
    pinecone_index = PineConeIndex(name="test-index", dimension=8, metric="cosine", cloud="aws", region="us-east-1")
    res = create_index(pinecone_index)
    assert res is not None

if __name__ == "__main__":
   main_create_index()
   pytest.main()
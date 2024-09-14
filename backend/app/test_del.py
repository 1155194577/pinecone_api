from db.db_operation import del_vectors, add_vectors
from db.base_models import Vector
def test_del_vectors_success():
    add_vectors("test_namespace", [Vector(id="vec1", values=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.7], metadata={"genre": "comedy"})])
    res = del_vectors("test_namespace", ["vec1"])
    assert res == True

def test_del_vectors_nonexistent_vector():
    del_vectors("test_namespace", ["nonexistent_vec"])
    res = del_vectors("test_namespace", ["nonexistent_vec"])
    assert res == False

def test_del_vectors_empty_namespace():
    res = del_vectors("", ["vec2"])
    assert res == False

def test_del_vectors_empty_vector_list():
    res = del_vectors("test_namespace", [])
    assert res == False

def test_del_vectors_invalid_vector_id():
    res = del_vectors("test_namespace", [""])
    assert res == False

def test_del_vectors_multiple_vectors():
    res = del_vectors("test_namespace", ["vec3", "vec4"])
    assert res == True

def test_del_vectors_special_characters():
    res = del_vectors("test_namespace", ["vec5"])
    assert res == True

def test_del_vectors_large_vector_id():
    large_id = "vec" + "x" * 1000
    res = del_vectors("test_namespace", [large_id])
    assert res == False

def test_del_vectors_invalid_namespace():
    res = del_vectors("invalid_namespace", ["vec6"])
    assert res == False

def test_del_vectors_mixed_valid_invalid_ids():
    res = del_vectors("test_namespace", ["vec7", "nonexistent_vec"])
    assert res == True
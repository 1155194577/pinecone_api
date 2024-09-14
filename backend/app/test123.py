from db.db_operation import add_vectors, del_vectors
from db.base_models import Vector

def test_add_vectors_success():
    res = add_vectors("test_namespace", [Vector(id="vec1", values=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8], metadata={"genre": "comedy"})])
    assert res == True

def test_add_vectors_duplicate():
    add_vectors("test_namespace", [Vector(id="vec2", values=[0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1], metadata={"genre": "action"})])
    res = add_vectors("test_namespace", [Vector(id="vec2", values=[0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1], metadata={"genre": "action"})])
    assert res == True

def test_add_vectors_empty_namespace():
    res = add_vectors("", [Vector(id="vec3", values=[0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4], metadata={"genre": "horror"})])
    assert res == False

def test_add_vectors_empty_vector_list():
    res = add_vectors("test_namespace", [])
    assert res == False

def test_add_vectors_invalid_vector():
    res = add_vectors("test_namespace", [Vector(id="", values=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], metadata={})])
    assert res == False

def test_add_vectors_large_vector():
    res = add_vectors("test_namespace", [Vector(id="vec4", values=[i * 0.1 for i in range(8)], metadata={"genre": "sci-fi"})])
    assert res == True

def test_add_vectors_special_characters():
    res = add_vectors("test_namespace", [Vector(id="vec5", values=[1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8], metadata={"genre": "drama", "special": "@#$%"})])
    assert res == True

def test_add_vectors_multiple_vectors():
    vectors = [
        Vector(id="vec6", values=[1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1], metadata={"genre": "thriller"}),
        Vector(id="vec7", values=[1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4], metadata={"genre": "romance"})
    ]
    res = add_vectors("test_namespace", vectors)
    assert res == True

def test_add_vectors_invalid_metadata():
    res = add_vectors("test_namespace", [Vector(id="vec8", values=[2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7], metadata={"genre": None})])
    assert res == False

def test_add_vectors_large_metadata():
    large_metadata = {str(i): "value" for i in range(1000)}
    res = add_vectors("test_namespace", [Vector(id="vec9", values=[2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0], metadata=large_metadata)])
    assert res == True


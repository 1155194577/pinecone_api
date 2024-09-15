from .db_operation import add_vectors, del_vectors, get_vectors,search_vectors
from ..base_models.db_base_models import Vector
import pytest
@pytest.mark.parametrize("namespace, vectors, expected", [
    ("test_namespace", [Vector(id="vec1", values=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8], metadata={"genre": "comedy"})], True),
    ("test_namespace", [Vector(id="vec2", values=[0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1], metadata={"genre": "action"})], True),
    ("", [Vector(id="vec3", values=[0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4], metadata={"genre": "horror"})], False),
    ("test_namespace", [], False),
    ("test_namespace", [Vector(id="", values=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], metadata={})], False),
    ("test_namespace", [Vector(id="vec4", values=[i * 0.1 for i in range(8)], metadata={"genre": "sci-fi"})], True),
    ("test_namespace", [Vector(id="vec5", values=[1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8], metadata={"genre": "drama", "special": "@#$%"})], True),
    ("test_namespace", [
        Vector(id="vec6", values=[1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1], metadata={"genre": "thriller"}),
        Vector(id="vec7", values=[1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4], metadata={"genre": "romance"})
    ], True),
    ("test_namespace", [Vector(id="vec8", values=[2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7], metadata={"genre": None})], False),
    ("test_namespace", [Vector(id="vec9", values=[2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0], metadata={str(i): "value" for i in range(1000)})], True),
])
def test_add_vectors(namespace, vectors, expected):
    res = add_vectors(namespace, vectors)
    assert res == expected


@pytest.mark.parametrize("namespace, vector_ids, expected", [
    ("ns1",["vec1"],1),
    ("ns1",["vec1","vec2"],2),
    ("ns1",["vec1","vec2","vec3"],3),
    ("ns1",["vec1","vec2","vec3","vec4"],4),
])
def test_get_vectors(namespace, vector_ids, expected):
    res = get_vectors(namespace, vector_ids)    
    assert res is not False
    assert len(res) == expected




@pytest.mark.parametrize("namespace, vector_ids, expected", [
    ("test_namespace", ["vec1"], True),
    ("test_namespace", ["nonexistent_vec"], False),
    ("", ["vec2"], False),
    ("test_namespace", [], False),
    ("test_namespace", [""], False),
    ("test_namespace", ["vec3", "vec4"], True),
    ("test_namespace", ["vec5"], True),
    ("test_namespace", ["vec" + "x" * 1000], False),
    ("invalid_namespace", ["vec6"], False),
    ("test_namespace", ["vec7", "nonexistent_vec"], True),
])
def test_del_vectors(namespace, vector_ids, expected):
    res = del_vectors(namespace, vector_ids)
    assert res == expected

@pytest.mark.parametrize("namespace, vector, expected", [
    ("test_namespace", Vector(id="vec1", values=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8], metadata={"genre": "comedy"}), 1),
    ("test_namespace", Vector(id="vec2", values=[0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1], metadata={"genre": "action"}), 1),
    ("test_namespace", Vector(id="vec4", values=[i * 0.1 for i in range(8)], metadata={"genre": "sci-fi"}), 1),
    ("test_namespace", Vector(id="vec5", values=[1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8], metadata={"genre": "drama", "special": "@#$%"}), 1),
    ("test_namespace", Vector(id="vec6", values=[1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1], metadata={"genre": "thriller"}), 1),
    ("test_namespace", Vector(id="vec7", values=[1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4], metadata={"genre": "romance"}), 1),
    ("test_namespace", Vector(id="vec9", values=[2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0], metadata={str(i): "value" for i in range(1000)}), 1),
])
def test_search_vectors(namespace, vector, expected):
    res = search_vectors(namespace, vector, expected)
    assert len(res) == expected


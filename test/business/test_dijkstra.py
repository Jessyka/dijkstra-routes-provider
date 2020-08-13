import pytest

from src.business.dijkstra import Dijkstra
from src.entity.edge import Edge


@pytest.fixture
def edges():
    return [
        Edge('A', 'B', 5),
        Edge('A', 'C', 10),
        Edge('B', 'C', 1),
        Edge('C', 'A', 1),
        Edge('C', 'B', 2),
        Edge('B', 'A', 3),
    ]


@pytest.fixture(scope="session", autouse=True)
def dijkstra():
    return Dijkstra()


def test_validate_steps_for_minimal_path_for_vertex_a_to_c(dijkstra, edges):
    minimal_path = dijkstra.find_path('A', 'C', edges)
    assert 2 == len(minimal_path)


def test_find_minimal_path_for_vertex_a_to_c(dijkstra, edges):
    minimal_path = dijkstra.find_path('A', 'C', edges)
    assert ('A' == minimal_path[0].initialVertex and 'B' == minimal_path[0].finalVertex
            and 'B' == minimal_path[1].initialVertex and 'C' == minimal_path[1].finalVertex)


def test_validate_minimal_distance_for_vertex_a_to_c(dijkstra, edges):
    minimal_path = dijkstra.find_path('A', 'C', edges)
    assert 6 == sum(item.weight for item in minimal_path)


def test_validate_steps_for_minimal_path_for_vertex_c_to_a(dijkstra, edges):
    minimal_path = dijkstra.find_path('C', 'A', edges)
    assert 1 == len(minimal_path)


def test_find_minimal_path_for_vertex_c_to_a(dijkstra, edges):
    minimal_path = dijkstra.find_path('C', 'A', edges)
    assert ('C' == minimal_path[0].initialVertex and 'A' == minimal_path[0].finalVertex)


def test_validate_minimal_distance_for_vertex_c_to_a(dijkstra, edges):
    minimal_path = dijkstra.find_path('C', 'A', edges)
    assert 1 == sum(item.weight for item in minimal_path)


def test_return_0_steps_when_no_path(dijkstra, edges):
    minimal_path = dijkstra.find_path('A', 'E', edges)
    assert 0 == len(minimal_path)


def test_return_0_steps_when_same_initial_and_final_vertex(dijkstra, edges):
    minimal_path = dijkstra.find_path('A', 'A', edges)
    assert 0 == len(minimal_path)

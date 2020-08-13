from src.entity.route import Route
from src.entity.edge import Edge

def test_return_0_when_get_distance_but_empty_path():
    route = Route('A', 'B')
    assert 0 == route.get_distance()

def test_return_weight_sum_when_get_distance():
    route = Route('A', 'B')
    route.path.append(Edge('A','C', 10))
    route.path.append(Edge('C','B', 5))
    assert 15 == route.get_distance()
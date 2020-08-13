from src.business.route_calculator import RouteCalculator


def test_validate_steps_for_minimal_path_for_vertex_a_to_b():
    # A => B: minimal path = one step
    route_calculator = RouteCalculator()
    minimal_path_a_to_b = route_calculator.find_path('A', 'B')
    assert 1 == len(minimal_path_a_to_b)


def test_find_minimal_path_for_vertex_a_to_b():
    # A => B: minimal path = one step
    route_calculator = RouteCalculator()
    minimal_path_a_to_b = route_calculator.find_path('A', 'B')
    assert ('A' == minimal_path_a_to_b[0].initialVertex and
            'B' == minimal_path_a_to_b[0].finalVertex)


def test_validate_steps_for_minimal_path_for_vertex_a_to_c():
    # A => C: minimal path = two steps
    route_calculator = RouteCalculator()
    minimal_path_a_to_c = route_calculator.find_path('A', 'C')
    assert 2 == len(minimal_path_a_to_c)


def test_find_minimal_path_for_vertex_a_to_c():
    # A => C: minimal path = two steps
    route_calculator = RouteCalculator()
    minimal_path_a_to_c = route_calculator.find_path('A', 'C')
    assert ('A' == minimal_path_a_to_c[0].initialVertex and 'B' == minimal_path_a_to_c[0].finalVertex
            and 'B' == minimal_path_a_to_c[1].initialVertex and 'C' == minimal_path_a_to_c[1].finalVertex)


def test_find_minimal_distance_for_invalid_vertex():
    route_calculator = RouteCalculator()
    distance = route_calculator.find_minimal_distance('C', 'O')
    assert 0 == distance


def test_find_minimal_distance_for_valid_vertex():
    route_calculator = RouteCalculator()
    distance = route_calculator.find_minimal_distance('A', 'C')
    assert 9 == distance

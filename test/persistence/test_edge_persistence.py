from src.persistence.edge_persistence import EdgePersistence

def test_validate_total_of_edge_data_from_json_file():
    persistence = EdgePersistence()
    edgesData = persistence.get_data()
    assert 9 == len(edgesData)


def test_validate_first_element_from_edge_data():
    persistence = EdgePersistence()
    edgesData = persistence.get_data()
    assert 'A' == edgesData[0].initialVertex and 'B' == edgesData[0].finalVertex and 5 == edgesData[0].weight
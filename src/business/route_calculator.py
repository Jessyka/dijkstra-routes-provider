from src.business.dijkstra import Dijkstra
from src.persistence.edge_persistence import EdgePersistence


class RouteCalculator:
    def __init__(self):
        edge_persistence = EdgePersistence()
        self.edges = edge_persistence.get_data()
        self.vertex = self.__get_all_vertex()
        self.minimal_path_calculator = Dijkstra()

    def __get_all_vertex(self):
        vertex = set([])
        for item in self.edges:
            vertex.add(item.initialVertex)
            vertex.add(item.finalVertex)
        return vertex

    def get_paths(self):
        return self.edges

    def show_routes(self):
        for item in self.edges:
            print(f'Begin: {item.initialVertex} End: {item.finalVertex} Distance Value: {item.weight}')

    def show_minimal_path(self, initial_vertex, final_vertex):
        minimal_path = self.minimal_path_calculator.find_path(initial_vertex, final_vertex, self.edges)
        if not minimal_path:
            print('No path found')

        else:
            for item in minimal_path:
                print(f'{item.initialVertex} ==> {item.finalVertex}')

    def find_path(self, initial_vertex, final_vertex):
        return self.minimal_path_calculator.find_path(initial_vertex, final_vertex, self.edges)

    def find_minimal_distance(self, initial_vertex, final_vertex):
        return sum(
            item.weight for item in self.minimal_path_calculator.find_path(initial_vertex, final_vertex, self.edges))

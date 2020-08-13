from src.entity.edge import Edge


class Dijkstra:
    def __init__(self):
        self.nodes = set([])
        self.distances = dict([])

    def find_path(self, initial_vertex, final_vertex, edges):
        route = []
        paths = dict([])
        self.__set_all_vertex(edges)
        self.__set_initial_distances(initial_vertex)

        while len(self.nodes):
            smallest_distance = sorted(self.nodes, key=self.__sort_nodes_by_distance)[0]
            self.nodes.discard(smallest_distance)

            if smallest_distance == final_vertex:
                while smallest_distance in paths:
                    path = self.__get_edge_by_initial_and_final_vertex(edges, paths[smallest_distance], smallest_distance)
                    route.append(path)
                    smallest_distance = paths[smallest_distance]
                break

            if self.distances[smallest_distance] == float('inf'):
                break

            for item in self.__get_vertex_neighbours(edges, smallest_distance):
                distance = self.distances[smallest_distance] + item.weight
                if distance < self.distances[item.finalVertex]:
                    self.distances[item.finalVertex] = distance
                    paths[item.finalVertex] = smallest_distance

        route.reverse()
        return route

    def __get_vertex_neighbours(self, edges, vertex):
        return [edge for edge in edges if edge.initialVertex == vertex]

    def __get_edge_by_initial_and_final_vertex(self, edges, initial_vertex, final_vertex):
        return next((edge for edge in edges if
                     (edge.initialVertex == initial_vertex and edge.finalVertex == final_vertex)), None)

    def __set_all_vertex(self, edges):
        self.nodes.clear()
        for item in edges:
            self.nodes.add(item.initialVertex)
            self.nodes.add(item.finalVertex)

    def __set_initial_distances(self, initial_vertex):
        self.distances.clear()
        inf = float('inf')

        for item in self.nodes:
            if item == initial_vertex:
                self.distances[item] = 0
            else:
                self.distances[item] = inf

    def __sort_nodes_by_distance(self, element):
        return self.distances[element]

    def __sort_nodes_by_distance(self, element):
        return self.distances[element]
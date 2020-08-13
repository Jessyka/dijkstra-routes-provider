import json
from src.entity.edge import Edge

class EdgePersistence:

    def get_data(self):
        edges = []
        try:
            with open('src/persistence/EdgesRepository.json') as json_file:
                data = json.load(json_file)
                for p in data['edges']:
                    edges.append(Edge(p['vertexBegin'], p['vertexEnd'], p['weight']))
        except:
            print('An error occurred when tried to read from edges repository file.')

        return edges

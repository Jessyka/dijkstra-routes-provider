
class Route:
    def __init__(self, initial, final):
        self.initialVertex = initial
        self.finalVertex = final
        self.path = []

    def get_distance(self):
        distance = 0
        for item in self.path:
            distance += item.weight

        return distance
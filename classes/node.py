{
    value: 5,
    edges: [Node(1), 2, 4]
}


class Node():
    value = None
    edges = []

    def __init__(self, value, edges=[]):
        self.value = value
        self.edges = edges

    def add_edge(self, value):
        self.edges.append(value)

    def __str__(self):
        return str(self.value)
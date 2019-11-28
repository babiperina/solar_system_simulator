class Sphere():
    """
            This class was used to represent a triangle
            by:Bárbara Perina
        """
    def __init__(self):
        pass

class Triangle():
    """
            This class was used to represent a triangle
            by:Bárbara Perina
        """
    def __init__(self, edges):
        self.arestas = (
            (2, 0),
            (1, 2),
            (0, 1)
        )

        self.edges = edges
        for edge in edges:
            print(edge)
            edgeList = list(edge)
            if edgeList[2] == 0:
                edgeList[2] = 1
                edge = tuple(edgeList)

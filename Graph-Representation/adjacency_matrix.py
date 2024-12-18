class Graph:
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.adj_matrix = [
            [0] * vertices for _ in range(vertices)
        ]  #  a matrix with dimensions V x V , V = no of vertices

    def add_edge(self, u, v):
        if u >= self.vertices or v >= self.vertices:
            return
        self.adj_matrix[u][v] = 1  # bidirectional graph
        self.adj_matrix[v][u] = 1

    def remove_edge(self, u, v):
        if u >= self.vertices or v >= self.vertices:
            return
        self.adj_matrix[u][v] = 0
        self.adj_matrix[v][u] = 0

    def has_edge(self, u, v):
        return self.adj_matrix[v][u] == 1

    def display(self):
        for row in self.adj_matrix:
            print(row)


g = Graph(6)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(0, 3)
g.add_edge(4, 3)
g.add_edge(5, 4)
print(g.has_edge(4, 1))
g.display()

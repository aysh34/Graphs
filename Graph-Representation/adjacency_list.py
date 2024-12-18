class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  # Number of nodes in the graph(value 0-4)
        self.adj_list = {
            i: [] for i in range(vertices)
        }  # i = vertex , [vertices with which i is connected]

    # to add an edges b/w two vertices u and v (undirected graph)
    def add_edge(self, u, v):
        if u >= self.vertices or v >= self.vertices:
            return
        self.adj_list[u].append(v)  # Add v to u's list of neighbors
        self.adj_list[v].append(u)  # Add u to v's list of neighbors

    def remove_edge(self, u, v):
        if v in self.adj_list[u]:
            self.adj_list[u].remove(v)
        elif u in self.adj_list[v]:
            self.adj_list[u].remove(u)
        else:
            return -1

    # to check if an edge exists between u and v
    def has_edge(self, u, v):
        return v in self.adj_list[u]

    #  to display the graph (adjacency list representation)
    def display(self):
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")


g = Graph(6)  # vertices are 0,1,2,3,4,5
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(0, 3)
g.add_edge(4, 3)
g.add_edge(5, 4)
print(g.has_edge(4, 1))
g.display()

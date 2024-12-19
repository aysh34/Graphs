from collections import deque


def bfsOfGraph(adj):
    # code here
    visited = set()
    res = []

    def bfs(adj, node, visited, res):
        q = deque([node])
        visited.add(node)
        res.append(node)

        while q:
            n = q.popleft()
            for neighbor in adj[n]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
                    res.append(neighbor)

    bfs(adj, 0, visited, res)
    return res


g1 = [[2, 3, 1], [0], [0, 4], [0], [2]]
ans1 = bfsOfGraph(g1)
print(ans1)

g2 = [[1], [0, 2, 3], [1], [1, 4], [3]]
ans2 = bfsOfGraph(g2)
print(ans2)

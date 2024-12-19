def dfsOfGraph(adj):
    res = []
    visited = set()

    def dfs(adj, node, visited, res):
        if node in visited:
            return
        visited.add(node)
        res.append(node)

        for n in adj[node]:
            if n not in visited:
                dfs(adj, n, visited, res)

    dfs(adj, 0, visited, res)
    return res


graph = [[2, 3, 1], [0], [0, 4], [0], [2]]
ans = dfsOfGraph(graph)
print(ans)  # [0, 2, 4, 3, 1]
graph2 = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
ans2 = dfsOfGraph(graph2)
print(ans2)  #  [0, 1, 2, 3, 4]

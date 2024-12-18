class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = {i:[] for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # BFS
        visited = set()
        q = deque([source])

        while q:
            node = q.popleft()
            if node == destination:
                return True
            if node not in visited:
                visited.add(node)
                for i in adj[node]: # explore its neighbors
                    if i not in visited:
                        q.append(i)
        return False



        
        
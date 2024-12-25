from typing import List
from collections import deque
class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool: # bfs
        def bfs(adj,node,visited):
            q = deque([(node,-1)]) # we append a tuple in q, tuple[0] = node tuple[1] = parent.  first node has no parent so -1
            visited[node] = True
            
            while q:
                # pop front 
                source , parent  = q.popleft()
                
                for i in adj[source]: # explore the neighbors of source/ current node
                    if visited[i] == False:
                        q.append((i,source))
                        visited[i] = True
                    elif visited[i] == True and i != parent: # i is not the parent of source but visited , this confirms the cycle.
                        return True
            return False
            
        visited = [False] * V
        for i in range(V):
            if visited[i] == False and bfs(adj,i,visited):
                return True
        return False

class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
        def isCycleDFS(adj,node,visited,parent):
            visited.add(node) 
            
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue 
                if neighbor in visited:
                    return True
                
                if isCycleDFS(adj,neighbor,visited,node):
                    return True
            
            return False

        visited = set()    
        for i in range(V): # graph can be disconnected, so using this loop
            if i not in visited and isCycleDFS(adj,i,visited,-1):
                return True
        
        return False


''' pseudo code 

Problem with simple dfs is we can not declare as cyclic graph on the basis of visited only.
When we are given with only two nodes in undirected graph, we declare this as cyclic as per our logic which is wrong.
So to tackle this, we pass a parent parameter this time.

Now during dfs, we come across such a node which we are going to explore is not the parent of current node and visited already as well. This shows the graph has cycle.

'''

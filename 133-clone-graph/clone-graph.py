"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None
        mp = {}  # key = original_node, value = clone

        def dfs(original_node):
            if original_node in mp:
                return mp[original_node]  # return corresponding clone
            clone = Node(original_node.val)
            mp[original_node] = clone

            for neighbor in original_node.neighbors:
                clone.neighbors.append(
                    dfs(neighbor)
                )  # a clone's neighbor must also be a clone
            return clone

        return dfs(node)

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodes = {} 
        x = 0
        if node is None:
            return node 
        seen = set()
        def dfs(node):
            copy = Node(node.val) 
            seen.add(node.val)
            if node.val in nodes:
                copy = nodes[node.val] 
            else:
                nodes[node.val] = copy 
            
            for adj in node.neighbors:
                if adj.val in seen:
                    copy.neighbors.append(nodes[adj.val])
                    continue 
                copy.neighbors.append(dfs(adj))
            
            return copy 

        copy_node = Node(node.val) 
        nodes[node.val] = copy_node 
        dfs(node) 
        return copy_node 
            
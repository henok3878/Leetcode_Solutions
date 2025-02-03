class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph) 
        colors = [None] * n 
        
        def dfs(curr):
            for adj in graph[curr]:
                if colors[adj] is None:
                    colors[adj] = -1 * colors[curr]
                    if not dfs(adj):
                        return False 
                elif(colors[adj] == colors[curr]):
                    return False 
                else:
                    continue 
            return True
        
        for i in range(n):
            if colors[i] is None:
                colors[i] = 1 
                if not dfs(i):
                    return False 
        return True 

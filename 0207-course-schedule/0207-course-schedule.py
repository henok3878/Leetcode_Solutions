class Solution:
    def canFinish(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)] 
        for u,v in edges:
            graph[v].append(u) 
        
        visited = set() 

        def dfs(node, curr_path):
            if node in curr_path:
                return False 
            elif node in visited:
                return True
            visited.add(node)
            curr_path.add(node)
            for adj in graph[node]:
                if( not dfs(adj, curr_path)):
                    return False 
            curr_path.remove(node) 
            return True 
        
        for i in range(n):
            if i not in visited:
                if not dfs(i, set()):
                    return False 
        return True 

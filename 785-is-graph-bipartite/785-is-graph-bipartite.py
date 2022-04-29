class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph)
        visited = [0] * n
        '''
            visited[i] = -1 => visited and colored white 
            visited[i] = 0 => not_visited 
            visited[i] = 1 => visited and colored black
        '''
        
        def dfs(i,p):
            if(visited[i] == p):
                return False
            elif(visited[i] == -1*p):
                return True
            visited[i] = -1*p
            for adj in graph[i]:
                if(not dfs(adj,-1*p)):
                    return False
            return True
        
        for i in range(n):
            if(visited[i] == 0 and not dfs(i,-1)):
                return False
            
        return True
                
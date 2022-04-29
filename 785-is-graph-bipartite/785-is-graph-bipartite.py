class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph)
        visited = [0] * n
        '''
            visited[i] = -1 => visited and colored white 
            visited[i] = 0 => not_visited 
            visited[i] = 1 => visited and colored black
        '''
        
        def bfs(i):
            q = collections.deque()
            q.append(i)
            visited[i] = -1
            while(len(q) > 0):
                
                pop = q.popleft()
                
                for adj in graph[pop]:
                    
                    if(visited[adj] == visited[pop]):
                        return False
                    elif(visited[adj] == 0):
                        visited[adj] = -1*visited[pop]
                        q.append(adj)
                        
            return True
        
        for i in range(n):
            if(visited[i] == 0 and not bfs(i)):
                return False
            
        return True
                
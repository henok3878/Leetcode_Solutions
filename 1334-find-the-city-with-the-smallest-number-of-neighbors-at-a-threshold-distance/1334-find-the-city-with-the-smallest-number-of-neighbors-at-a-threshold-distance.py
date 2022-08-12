class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0 
        
        graph = defaultdict(list) 
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))
            dist[u][v] = w 
            dist[v][u] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) 
        
        count,ans = n,0 
        for i in range(n):
            curr_count = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold: 
                    curr_count += 1
            if curr_count  <= count:
                ans = i 
                count = curr_count 
        #print(dist)
        return ans 
                
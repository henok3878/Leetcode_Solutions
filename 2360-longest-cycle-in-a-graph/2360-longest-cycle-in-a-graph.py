class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        
        graph = {} 
        for u,v in enumerate(edges):
            if v != -1:
                graph[u] = v  
        
        def dfs(node, curr_path, dist):
            #print(node,curr_path, dist, end = " ")
           
            if node in curr_path:
                #print("cycle at node: ", node, dists)
                d = dist - curr_path[node]
                dists[node] = max(dists[node], d)
                return
            if node in visited:
                #print(node, visited)
                return 
            visited.add(node)
            if node in graph:
                curr_path[node] = dist  
                dfs(graph[node], curr_path, dist + 1)
            return 0
        
        n = len(edges)
        dists = [0] * n 
        visited = set() 
        
        for i in range(n):
            dfs(i, defaultdict(int),0)
        
        #print(dists)
        longest = max(dists)
        return longest if longest > 1 else -1 
       
    
                
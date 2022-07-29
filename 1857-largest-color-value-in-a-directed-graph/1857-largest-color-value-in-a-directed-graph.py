class Solution:
    
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:        
        def build_graph():
            for u, v in edges:
                graph[u].append(v)
                if u == v:
                    return -1
                
        def update_color_values(u, v):
            for i in range(26):
                path_value = color_values[v][i]
                if colors[u] == chr(ord('a') + i):
                    path_value += 1
                color_values[u][i] = max(color_values[u][i], path_value)
        
        n = len(colors)
        visited = set() 
        curr_path =set()
        color_values=[[1 if colors[node] == chr(ord('a') + i) else 0 for i in range(26)] for node in range(n)]

        
        def dfs(root):
            if root in visited:
                return
            if root in curr_path:
                return -1 
            curr_path.add(root)
            for child in graph[root]:
                if dfs(child) == -1:
                    return -1 
                update_color_values(root, child)
                
            curr_path.remove(root)
            visited.add(root)
        
        graph = defaultdict(list)
        build_graph()
        largest = 0
        for node in range(n):
            if dfs(node) == -1:
                return -1 
            largest = max(largest,max(color_values[node]))
            
        return largest
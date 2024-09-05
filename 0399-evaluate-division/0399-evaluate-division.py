class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        n = len(equations)
        for i in range(n):
            u,v = equations[i]
            graph[u].append([v, values[i]])
            graph[v].append([u, 1/ values[i]])
        ans = []
        visited = set()
        def dfs(curr_node, last_node):
            if curr_node == last_node:
                return 1
            visited.add(curr_node)
            for adj, w in graph[curr_node]:
                if adj in visited:
                    continue 
                res = dfs(adj, last_node)
                if res > 0:
                    return res * w 
            return -1

            
        
        for u,v in queries:
            ans.append(dfs(u, v) if len(graph[u]) > 0 and len(graph[v]) > 0 else -1)
            visited.clear()
        return ans 
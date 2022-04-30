class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        n = len(equations)
        for idx in range(n):
            eq = equations[idx]
            u,v,cost = eq[0], eq[1], values[idx]
            graph[u].append((v,cost))
            graph[v].append((u,1/cost))
            
       
        def is_reachable(st,end,res):
            if(st not in graph):
                return -1
            elif(st == end):
                return res
            visited[st] = True
            
            for adj in graph[st]:
                if(not visited[adj[0]]):
                    temp = is_reachable(adj[0],end,adj[1] * res)
                    if(temp != -1):
                        return temp
            return -1
            
        ql = len(queries)
        ans = [-1]*ql
        for i in range(ql):
            q = queries[i]
            u,v = q[0],q[1]
            visited = defaultdict(bool)
            ans[i] = is_reachable(u,v,1)
    
        return ans
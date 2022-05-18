class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
        # print(graph)
        
        ans = []
        first_time = [0] * n
        lowest_nei_time = [0] * n
        visited = [False] * n
        time = 0
        def dfs(node,parent):
            nonlocal time
            visited[node] = True
            time += 1
            first_time[node] = time
            lowest_nei_time[node] = time
            
            for v in graph[node]:
                if v == parent:
                    continue
                if(not visited[v]):
                    dfs(v,node)
                    lowest_nei_time[node] = min(lowest_nei_time[node],lowest_nei_time[v])
                else:  
                    lowest_nei_time[node] = min(lowest_nei_time[node],first_time[v])
                if(first_time[node] < lowest_nei_time[v]):
                    ans.append([node,v])
        
        dfs(0,-1)
        # print(first_time)
        # print(lowest_nei_time)
        return ans
            
      
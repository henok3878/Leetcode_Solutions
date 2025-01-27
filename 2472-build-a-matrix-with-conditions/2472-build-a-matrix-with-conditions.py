class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def bfs(in_degree, graph):
            orders = [] 
            q = deque()
            n = len(in_degree) 
            for i in range(n): 
                if in_degree[i] == 0:
                    q.append(i)
            
            while q: 
                curr = q.popleft() 
                orders.append(curr)
                for adj in graph[curr]:
                    in_degree[adj] -= 1 
                    if(in_degree[adj] == 0):
                        q.append(adj) 
            if len(orders) == n:
                return orders 
            return None 
        
        col_graph = defaultdict(list) 
        row_graph = defaultdict(list) 
        indegree_col = [0] * k 
        indegree_row = [0] * k 

        for u,v in colConditions:
            col_graph[u-1].append(v-1)
            indegree_col[v-1] += 1 

        for u,v in rowConditions:
            row_graph[u-1].append(v-1) 
            indegree_row[v-1] += 1
       
        col_ordering = bfs(indegree_col, col_graph) 
        row_ordering = bfs(indegree_row, row_graph)
        if(col_ordering is None or row_ordering is None):
            return []
        map_val_row = [0] * k 
        for i, val in enumerate(row_ordering):
            map_val_row[val] = i 
        ans = [[0]*k for _ in range (k)]
        for col_i, val in enumerate(col_ordering):
            row_i = map_val_row[val] 
            ans[row_i][col_i] = val + 1
        return ans 

        


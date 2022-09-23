class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        sub_tree = [0] * n 
        sum_dist = [0] * n 
        
        tree = defaultdict(list) 
        for u,v in edges:
            tree[u].append(v) 
            tree[v].append(u) 
        
        def dfs1(node, p):
            sub_tree[node] = 1 
            for adj in tree[node]:
                if adj != p:
                    dfs1(adj,node) 
                    sub_tree[node] += sub_tree[adj] 
                    sum_dist[node] += (sum_dist[adj] + sub_tree[adj])
        def dfs2(node,p):
            for adj in tree[node]:
                if adj != p:
                    adj_size = sub_tree[adj] 
                    out_side_adj = n - adj_size 
                    adj_contb = sum_dist[adj] + adj_size
                    sum_dist[adj] += (sum_dist[node] - adj_contb) + out_side_adj
                    dfs2(adj,node) 
                    
        dfs1(0,-1) 
        # print(sub_tree)
        # print(sum_dist)
        dfs2(0,-1)
        # print(sum_dist)
            
        return sum_dist
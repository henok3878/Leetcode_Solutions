from math import factorial
class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:        
        tree = defaultdict(list) 
        n = len(prevRoom)
        for u,v in enumerate(prevRoom):
            if u == 0:
                continue 
            tree[v].append(u) 
        # print(tree)
        sub_tree = [1] * n 
        sub_ways = [1] * n 
        
        MOD, M = 10**9 + 7, 10**5
        facts = [1]*(M+1)
        for i in range(1, M+1):
            facts[i] = (facts[i-1] * i) % MOD

        facts_inv = [1]*M + [pow(facts[M], MOD - 2, MOD)]
        for i in range(M-1, 0, -1):
            facts_inv[i] = facts_inv[i+1]*(i+1) % MOD
             
        def helper(node):
            ways = 1
            for adj in tree[node]:
                helper(adj)
                # print(node, adj, sub_tree[node], sub_tree[adj])
                sub_tree[node] += sub_tree[adj] 
                ways *= facts_inv[sub_tree[adj]] % MOD 
                ways *= sub_ways[adj]
            sub_ways[node] = ways * facts[sub_tree[node] - 1]
            sub_ways[node] %= MOD
            
        helper(0) 
        return sub_ways[0] 
    
    
    """
    [-1,0,1,1,2,2,3,3,0,8,8, 10,10,0, 13,13]
      0 1 2 3 4 5 6 7 8 9 10 11 12 13 14, 15 
    
    """
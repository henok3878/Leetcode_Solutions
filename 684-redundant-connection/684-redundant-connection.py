class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n + 1) 
        
        for u,v in edges:
            if not uf.union(u,v):
                return u,v
        
        
        

class UnionFind:
    
    def __init__(self,n):
        self.parents = [i for i in range(n)]
        self.ranks = [0] * n  
    
    def find(self,x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x]) # path compression 
        return self.parents[x] 
    
    def union(self,u,v):
        u_p = self.find(u) 
        v_p = self.find(v) 
        
        if u_p == v_p:
            return False 
        elif self.ranks[u_p] > self.ranks[v_p]:
            self.parents[v_p] = u_p 
        elif self.ranks[u_p] < self.ranks[v_p]:
            self.parents[u_p] = v_p 
        else:
            self.parents[v_p] = u_p 
            self.ranks[u_p] += 1 
        return True 
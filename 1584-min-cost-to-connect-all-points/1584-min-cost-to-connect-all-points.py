class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = UnionFind(n)
        
        edges = []
        for p1 in range(n):
            for p2 in range(p1 + 1, n):
                point1 = points[p1]
                point2 = points[p2]
                edge = [p1,p2,abs(point1[1]-point2[1]) + abs(point1[0] - point2[0])]
                edges.append(edge)
                
        edges.sort(key= lambda x: x[2])
        ans = 0
        used = 0
        idx = 0
        while(used < n and idx < len(edges)):
            edge = edges[idx]
            if(uf.union(edge[0],edge[1])):
                ans += edge[2]
                used += 1
            idx += 1
        
        return ans
        
        
class UnionFind:
    
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [0]*n
        
    def find(self,el):
        if(self.parents[el] != el):
            self.parents[el] = self.find(self.parents[el])
        return self.parents[el]
        
    def union(self,el1, el2):
        p1 = self.find(el1)
        p2 = self.find(el2)
        
        if(p1 == p2):
            return False
        if(self.ranks[p1] > self.ranks[p2]):
            self.parents[p2] = p1
        elif(self.ranks[p2] > self.ranks[p1]):
            self.parents[p1] = p2
        else:
            self.parents[p1] = p2
            self.ranks[p1] += 1
            
        return True
        
 
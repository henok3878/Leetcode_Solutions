class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)
        for pair in pairs:
            uf.union(pair[0],pair[1])
        
        componentsIdx = defaultdict(list)
        compChar = defaultdict(list)

        for i in range(n):
            root = uf.find(i)
            componentsIdx[root].append(i)
            compChar[root].append(s[i])
        
        for i in compChar:
            compChar[i].sort()
        
        ans = [' ']*n
        for root, comp in compChar.items():
            idx = 0
            for i in componentsIdx[root]:
                ans[i] = comp[idx]
                idx += 1
        
        return ''.join(ans)
        
        
        
        
        
class UnionFind:
    
    def __init__(self,n):
        self.parents = [i for i in range(n)]
        self.ranks = [0]*n
    
    def find(self,el):
        if(self.parents[el] != el):
            self.parents[el] = self.find(self.parents[el])
        return self.parents[el];
    
    def union(self,el1, el2):
        p1 = self.find(el1)
        p2 = self.find(el2)
        if(p1 == p2):
            return False
        if(self.ranks[p1] > self.ranks[p2]):
            self.parents[p2] = p1
        elif(self.ranks[p1] < self.ranks[p2]):
            self.parents[p1] = p2
        else:
            self.parents[p1] = p2
            self.ranks[p1] += 1
        return True
    
    
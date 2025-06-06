class UnionFind:
    def __init__(self, N):
        self.root = list(range(N))

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if y > x:
            self.root[y] = x
        else:
            self.root[x] = y


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind(26)
        a_idx = ord("a")
        n, m = len(s1), len(baseStr)
        for i in range(n):
            uf.union(ord(s1[i]) - a_idx, ord(s2[i]) - a_idx)
        ans = ""
        for x in baseStr:
            ans += chr(uf.find(ord(x) - a_idx) + a_idx)
        return ans

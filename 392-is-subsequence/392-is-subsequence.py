class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        maps = defaultdict(list)
        for i,c in enumerate(t):
            maps[c].append(i)        
        last = -1
        for c in s:
            idx = bisect_right(maps[c],last)
            if idx >= len(maps[c]):
                return False 
            else:
                last = maps[c][idx]
        return True 
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        dig_idx = defaultdict(deque)
        for i,c in enumerate(s):
            dig_idx[int(c)].append(i) 
        
        for c in t:
            c = int(c)
            if len(dig_idx[c]) == 0:
                return False 
            curr_idx = dig_idx[c][0] 
            for i in range(c):
                if len(dig_idx[i]) > 0 and dig_idx[i][0] < curr_idx:
                    return False 
            dig_idx[c].popleft()
        return True 
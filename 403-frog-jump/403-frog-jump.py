class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        last = stones[-1] 
        s_i = defaultdict(lambda: -1) 
        
        for i,stn in enumerate(stones):
            s_i[stn] = i 
        
        if stones[0] - stones[1] > 1:
            return False     
        
        @cache 
        def helper(idx,prev):
            if idx == len(stones)-1:
                return True 
            if prev == 0:
                next_unit = stones[idx] + 1
                if s_i[next_unit] != -1:
                    if helper(s_i[next_unit], 1):
                        return True 
                return False 
            for jump in range(prev - 1, prev + 2):
                next_unit = stones[idx] + jump
                if s_i[next_unit] != -1:
                    if helper(s_i[next_unit], jump):
                        return True 
            return False 
        
        return helper(0,0)
            
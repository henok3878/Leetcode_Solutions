class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        last = stones[-1] 
        stones_unit = set(stones)
        @cache 
        def helper(unit,prev):
            if unit == last:
                return True 
            if prev == 0:
                next_unit = unit + 1
                if next_unit in stones_unit:
                    if helper(next_unit, 1):
                        return True 
                return False 
            for jump in range(prev - 1, prev + 2):
                next_unit = unit + jump
                if next_unit in stones_unit:
                    if helper(next_unit,jump):
                        return True 
            return False 
        
        return helper(0,0)
            
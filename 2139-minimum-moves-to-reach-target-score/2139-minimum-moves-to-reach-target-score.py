class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        ans = 0
        while maxDoubles and target  > 1: 
            if target % 2 == 1:
                target -= 1 
                ans += 1 
            target //= 2 
            ans += 1
            maxDoubles -= 1             
        return ans + (target - 1)  
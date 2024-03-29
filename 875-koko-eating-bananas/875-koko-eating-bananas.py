class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        def is_pos(k):
            total = 0 
            for pile in piles:
                total += ceil(pile / k) 
            return total <= h 
        best = -1 
        low,high = 1, 10**9 
        while low <= high:
            mid = (low + high) // 2 
            if is_pos(mid):
                best = mid 
                high = mid - 1
            else:
                low = mid + 1 
                
        return best 
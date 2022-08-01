class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        
        @cache 
        def helper(l,h):
            if l >= h:
                return 0 
            lower = helper(l + 1, h) + piles[l] 
            higher = helper(l, h - 1) + piles[h] 
            
            return max(lower, higher)
        
        half = sum(piles) // 2  
        return helper(0, len(piles) -1 ) > half 
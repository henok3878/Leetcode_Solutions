class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consec_odds = 0
        for num in arr:
            if num % 2 == 1:
                consec_odds += 1 
            else:
                consec_odds = 0 
            if consec_odds >= 3:
                return True 
        return False 
     
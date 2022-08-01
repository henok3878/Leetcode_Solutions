class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        @cache 
        def play(l,r):
            if l > r:
                return 0 
            pick_first = nums[l] - play(l + 1, r) 
            pick_last = nums[r] - play(l, r - 1) 
            
            return max(pick_first, pick_last) 
        
        return play(0,len(nums) - 1) >= 0  
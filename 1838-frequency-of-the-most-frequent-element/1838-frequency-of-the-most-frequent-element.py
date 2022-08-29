class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort() 
        max_freq = 1 
        l, r = 0,1
        while r < len(nums):
            diff = nums[r] - nums[r - 1]
            if k >= diff*(r - l):
                k -= diff*(r - l) 
                r += 1
            else: 
                k += nums[r - 1] - nums[l]
                l += 1 
            max_freq = max(r - l, max_freq)    
        return max_freq 
    
    
    """
    1,2,4 
    2,2,4 , k = 4 
    4,4,4,6
    
    """
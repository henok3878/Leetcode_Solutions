class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        n = len(nums)
        evens  = [0] * (n + 1)
        odds = [0] * (n + 1)
        for i in range(1,n+1):
         
            evens[i] = max(evens[i-1],odds[i-1] - nums[i-1])
            odds[i] = max(odds[i-1],evens[i-1] + nums[i-1])
            
        return max(evens[n],odds[n])
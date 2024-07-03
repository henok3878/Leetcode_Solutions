class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort() 
        n = len(nums) 
        if(n <= 4):
            return 0
        mn_diff = float('inf')
        for prefix in range(4):
            suffix = 3 - prefix 
            mn_diff = min(mn_diff, nums[n - suffix - 1] - nums[prefix])
        return mn_diff 
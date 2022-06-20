class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return 0
        nums.sort()
        ans = 10**10
        for i in range(4):
            ans = min(ans, nums[n- 1 - ( 3 - i)] - nums[i])  
        return ans
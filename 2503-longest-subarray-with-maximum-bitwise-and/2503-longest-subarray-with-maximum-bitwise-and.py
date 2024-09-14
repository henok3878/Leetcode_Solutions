class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = max(nums)
        cnt = 0 
        ans = 0 
        i = 0 
        while i < len(nums):
            if (mx & nums[i] >= mx):
                cnt += 1 
            else:
                cnt = 0
            ans = max(ans, cnt)
            i += 1 

        return ans 

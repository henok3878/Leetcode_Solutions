class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = max(nums)
        cnt = 0 
        ans = 0 
        for num in nums:
            if mx == num:
                cnt += 1 
            else:
                cnt = 0 
            ans = max(ans, cnt) 
            
        return ans 

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        curr = 0 
        MX = 10**5 
        seen = [None] * (MX + 1 )
        n = len(nums)
        l = 0
        ans = 0
        for i in range(n):
            if (not (seen[nums[i]] is None)):
                p_i = seen[nums[i]] 
                while l <= p_i:
                    curr -= nums[l] 
                    l += 1 
            curr += nums[i] 
            if(i - l + 1 == k):
                ans = max(ans, curr)
                curr -= nums[l]
                l += 1 
            seen[nums[i]] = i
        return ans 

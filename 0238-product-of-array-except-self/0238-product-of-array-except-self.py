class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        suffix = [1] * n 
        suffix[-1] = nums[-1] 
        for i in range(n-2, -1, -1):
            suffix[i] *= suffix[i + 1] * nums[i]
        prefix = nums[0] 
        ans = [0] * n
        ans[0] = suffix[1]
        for i in range(1, n - 1):
            ans[i] = prefix * suffix[i + 1] 
            prefix *= nums[i]
        ans[-1] = prefix
        return ans 

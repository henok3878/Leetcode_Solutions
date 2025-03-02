class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        suffix = [1] * n 
        suffix = nums[-1]
        ans = [0] * n
        for i in range(n-2, -1, -1):
            ans[i] = suffix 
            suffix *= nums[i] 

        prefix = nums[0] 
        for i in range(1, n - 1):
            ans[i] *= prefix 
            prefix *= nums[i]
        ans[-1] = prefix
        return ans 

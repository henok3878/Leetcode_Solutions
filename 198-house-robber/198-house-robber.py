class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev, curr = 0,0
        for i in range(n):
            prev, curr= curr,max(nums[i] + prev,curr)
        
        return curr
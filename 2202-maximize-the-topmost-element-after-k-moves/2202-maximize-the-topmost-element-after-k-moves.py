class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return -1 if k % 2 == 1 else nums[0]
        if k > len(nums):
            return max(nums)
        max_elem = -1 
        i = 0 
        while i <= k - 2 and i < len(nums):
            max_elem = max(max_elem, nums[i]) 
            i += 1 
        if k < len(nums):
            max_elem = max(max_elem, nums[k])
        
        return max_elem 
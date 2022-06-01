class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        p = 0
        for i,num in enumerate(nums):
            nums[i] += p
            p = nums[i]
        return nums
            
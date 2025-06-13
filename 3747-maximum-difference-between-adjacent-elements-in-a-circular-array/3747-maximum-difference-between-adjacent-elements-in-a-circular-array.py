class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        ans = max(abs(nums[-1]-nums[0]), max(abs(nums[i] - nums[i+1]) for i in range(len(nums)-1)))
        return ans 
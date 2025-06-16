class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        smallest_to_left = [float('inf')] * n 
        mn = float('inf')
        for i in range(n):
            smallest_to_left[i] = mn 
            mn = min(nums[i], mn)
        best = max(nums[i] - smallest_to_left[i] for i in range(n)) 
        return best if best > 0 else -1 

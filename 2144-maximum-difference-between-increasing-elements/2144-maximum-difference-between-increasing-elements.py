class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mn = float('inf')
        best = float('-inf')
        for num in nums:
            best = max(best,num - mn)
            mn = min(num, mn)
        return best if best > 0 else -1 

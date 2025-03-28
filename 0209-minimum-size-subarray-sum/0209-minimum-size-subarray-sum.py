class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0 
        curr = 0
        best = float('inf')
        for right in range(n):
            curr += nums[right] 
            while left <= right and curr >= target:
                best = min(best, right - left + 1) 
                curr -= nums[left]
                left += 1 
        return best if best != float('inf') else 0
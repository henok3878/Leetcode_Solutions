class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        hops = [float('inf')] * n 
        hops[0] = 0 
        for i in range(n):
            jump = min(nums[i] + 1, n-i) 
            for j in range(jump):
                hops[i + j] = min(hops[i + j], hops[i] + 1) 

        return hops[-1]
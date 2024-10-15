class Solution:
    def rob(self, nums: List[int]) -> int:
        prevs = [0] * 2 
        for i in range(len(nums)):
            curr = max(prevs[0] + nums[i], prevs[1]) 
            prevs[0] = prevs[1] 
            prevs[1] = curr 
        return max(prevs) 



"""
For each house we have two options: 1. skip 2. rob 

if we rob: curr = can_make[i - 2] + curr
if we plan to skip: curr = can_make[i-1]

For this house: max(can_make[i - 2] + curr, can_make[i-1])

# we gotta be mindful of the negative indexing for i < 2

Time: O(N) 
space: O(1)
"""
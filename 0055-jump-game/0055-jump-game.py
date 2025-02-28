class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0
        for i,num in enumerate(nums):
            if i > curr: 
                return False 
            curr = max(i + num, curr) 
        return True 
     
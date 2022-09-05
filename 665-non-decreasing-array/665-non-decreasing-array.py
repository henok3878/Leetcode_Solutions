class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        used = False 
        max_sofar = float('-inf')
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                if used: 
                    return False 
                elif max_sofar > nums[i]: 
                    nums[i] = nums[i-1]
                used = True
            max_sofar = max(max_sofar,nums[i-1]) 
        
        return True 
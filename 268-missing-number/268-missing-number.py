class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sets = set(nums)
        n = len(nums) + 1
        for i in range(n):
            if i not in sets:
                return i
        return -1
        
    
    """
    0000
    0001
    0001
    """
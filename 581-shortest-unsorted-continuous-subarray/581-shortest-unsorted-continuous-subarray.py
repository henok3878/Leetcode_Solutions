class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0, n -1
        sorted_nums = sorted(nums)
        
        while(l < n and sorted_nums[l] == nums[l]):
            l += 1
        while(r >= 0 and sorted_nums[r] == nums[r]):
            r -= 1
        if(r <= l):
            return 0
        return r - l + 1
    
    
    """
    5,6,7,8,1,2,3
    """    
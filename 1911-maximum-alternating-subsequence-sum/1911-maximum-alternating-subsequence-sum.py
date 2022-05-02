class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        n = len(nums)
        even  = 0
        odd = 0
        for i in range(1,n+1):
            temp = even
            even = max(even,odd - nums[i-1])
            odd = max(odd,even + nums[i-1])
            
        return max(even,odd)
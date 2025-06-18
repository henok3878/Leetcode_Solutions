class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort() 
        ans = [ nums[i:i + 3] if nums[i + 2] - nums[i] <= k else [-1,-1,-1] for i in range(0,len(nums)-2, 3)] 
        not_valid = any(row == [-1,-1,-1] for row in ans)
        return [] if not_valid else ans 
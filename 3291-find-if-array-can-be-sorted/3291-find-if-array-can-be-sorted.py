class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        def cnt(num):
            return bin(num).count('1')
        for i in range(n-1):
            for j in range(1,n-i):
                if nums[j-1] > nums[j]:
                    if cnt(nums[j-1]) == cnt(nums[j]):
                        nums[j-1],nums[j] = nums[j], nums[j-1]
                    else:
                        return False
        return True 

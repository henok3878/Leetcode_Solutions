class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l,r = 0, n - 1
        while(l < n and r > l):
            #print(nums)
            if nums[l] % 2 == 1:
                while(nums[r] % 2 == 1 and r > l):
                    r -= 1
                if(r >= 0):
                    nums[l],nums[r] = nums[r],nums[l]
                    r -= 1
                    l += 1
            elif nums[l] % 2 == 0:
                l += 1
        return nums
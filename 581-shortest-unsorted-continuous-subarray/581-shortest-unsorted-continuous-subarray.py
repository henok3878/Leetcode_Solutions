class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l,lMax = -1,-(10**6)
        for i,num in enumerate(nums):
            if num > lMax:
                lMax = num
            elif num < lMax:
                l = i
        r,rMin = n, 10**6
        
        for i in range(n-1,-1,-1):
            num = nums[i]
            if num < rMin:
                rMin = num
            elif num > rMin:
                r = i
        if l == -1 and r == n:
            return 0
        #print(l,r)
        return l - r  + 1
    
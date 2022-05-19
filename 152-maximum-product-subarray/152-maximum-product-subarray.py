class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        MIN = -1*(10 ** 10)
        neg, pos = (1,MIN)
        n = len(nums)
        ans = MIN
        for i in range(n):
            
            if nums[i] <= 0:
                t = pos 
                pos = neg * nums[i]
                neg = t * nums[i]
                neg = min(neg,nums[i])
            else:
                pos *= nums[i]
                neg *= nums[i]
                pos = max(pos,nums[i])
                
            ans = max(pos,ans)
            
        return ans
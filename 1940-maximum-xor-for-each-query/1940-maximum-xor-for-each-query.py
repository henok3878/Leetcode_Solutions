class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num 
        ans = []
        mx_xor = (1 << maximumBit) - 1 # all 1's 
        for i in range(len(nums)-1,-1,-1):
            ans.append(xor ^ mx_xor) 
            xor = xor ^ nums[i]
        return ans

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num 
        nums+= [0] 
        ans = []
        for i in range(len(nums)-1,0,-1):
            xor = xor ^ nums[i]
            curr_ans = 0
            for bit in range(maximumBit):
                if ((xor >> bit) & 1) == 0:
                    curr_ans |= (1 << bit) 
            ans.append(curr_ans) 
        return ans

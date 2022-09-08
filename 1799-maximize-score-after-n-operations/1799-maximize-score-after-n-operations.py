class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        def gcd(a,b):
            if a == 0:
                return b 
            return gcd(b % a, a) 
        def set_bit(n,i):
            n |= 1 << i
            return n 
        def toogle_bit(n,i):
            n ^= 1 << i
            return n 
        def get_bit(n,i):
            return n & 1 << i != 0
        def get_score(i,a,b):
            return i * gcd(a,b) 
        
        @cache 
        def helper(idx,mask):
            if idx == len(nums) // 2:
                return 0
            res = 0 
            for i in range(len(nums)):
                if get_bit(mask,i):
                    continue 
                mask = set_bit(mask,i)
                for j in range(i + 1, len(nums)):
                    if get_bit(mask,j):
                        continue 
                    mask = set_bit(mask,j)
                    res = max(res, helper(idx + 1,mask) + get_score(idx + 1,nums[i],nums[j]))
                    mask = toogle_bit(mask, j)
                mask = toogle_bit(mask,i) 
            return res 
        
        return helper(0,0)
        
        """
        mask: to keep track of used elements 
        
        set(n,i):
            n |= 1 << i 
        un_set(n,i):
            n &= (~(1 << i))
        toggle(n,i):
            n ^= (1 << i)
        
        
        """
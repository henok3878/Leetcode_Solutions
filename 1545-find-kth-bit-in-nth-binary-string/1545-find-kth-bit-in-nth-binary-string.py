class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def helper(size, invert,k):
            if size == 1:
                return "1" if invert else '0' 
            prv_size = size // 2 
            mid = prv_size + 1 
            if mid == k:
                return "0" if invert else "1" 
            elif k < mid: 
                return helper(prv_size,invert,k) 
            else:
                return helper(prv_size, not invert,mid - (k%mid))
        
        return helper(2**n - 1, False,k)
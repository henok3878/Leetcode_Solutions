class Solution:
    def minEnd(self, n: int, x: int) -> int:
        ans = x
        n -= 1
        for i in range(55):
            if (x >> i) & 1 == 0:
                # ith bit is zero 
                if (n & 1):
                    ans |= (1 << i)
                n >>= 1
        return ans 


        


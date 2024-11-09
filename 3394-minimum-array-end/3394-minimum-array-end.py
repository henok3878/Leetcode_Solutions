class Solution:
    def minEnd(self, n: int, x: int) -> int:
        '''
        observations:
        - x is the first element 
        - for elem y, the ff should hold (y & x) = x
        '''
        ans = x
        n -= 1
        j = 0
        for i in range(64):
            if (x >> i) & 1 == 0:
                # ith bit is zero 
                if (n & (1 << j)):
                    ans |= (1 << i)
                j += 1
        return ans 


        


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n < 3:
            return 1
        ppp,pp,p = 0,1,1
        for i in range(3,n + 1):
            curr = ppp + pp + p
            ppp,pp,p = pp,p,curr
            
        return p
        
        
        
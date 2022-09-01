class Solution:
    def numOfArrays(self, n: int, m: int, K: int) -> int:
        
        mod = 10**9 + 7 
        @cache 
        def helper(p,i,k):
            if i == 0:
                return int(k == 0)  
            res = 0
            for c in range(1, m + 1):
                res += helper(max(c,p),i - 1, k - int(p < c))
                res %= mod 
            return res 
        
        return helper(0,n,K) 

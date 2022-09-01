class Solution:
    def numOfArrays(self, n: int, m: int, K: int) -> int:
        
        mod = 10**9 + 7 
        # stack = []
        @cache 
        def helper(p,i,k):
            if i == 0:
                #print(stack,k) 
                return int(k == 0)  
            
            res = 0
            for c in range(1, m + 1):
                # stack.append(c)
                res += helper(max(c,p),i - 1, k - int(p < c))
                res %= mod 
                # stack.pop()

            return res 
        
        return helper(0,n,K) 
    
    """
    [1, 2, 1, 2, 2]
    
    """
    
            
            
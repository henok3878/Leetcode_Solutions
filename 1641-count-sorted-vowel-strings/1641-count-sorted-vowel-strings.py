class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        
        dp =  [1]*5
        for i in range(n):
            for l in range(1,5):
                dp[l] += dp[l-1]
            
        return dp[4]
        
        """
        n = 1, 
        a,e,i,o,u
        
        n = 2 
        
        a (a,e,i,o,u) => 1  1   1 
        e (a,e,i,o,u) => 2  3   4 
        i (a,e,i,o,u) => 3  6   10
        o (a,e,i,o,u) => 4  10  20
        u (a,e,i,o,u) => 5  15  35
        
        sum = 1 + 2 + 3 + 4 + 5 
            = 15 
        
        aa   2 
        ae
        ee
        
        n = 3 
           a 
        a(--) 1 
           a or e  
        e(--) 3 
        i(--) 6 
        o(--) 10
        u(--) 15 
        
        sum = 1 + 3 + 6 + 10 + 15 
            = 35
        """
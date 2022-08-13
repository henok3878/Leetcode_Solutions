class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        "babgbag", t = "bag" 
        
        
        BruteForce: (Method 1)
        
        1) Generate all subsequences (2^n subsequences) 
        2) For each check if they are equal with t 
        3) if equal increment counter 
        
        TimeComplexity: O(n*2^n) 
        Space: Function call stack: O(N)

        
        Method2: 
        
        "babgbag", t = "bag" 
         ^              ^ 
         abgbag, ag | abgbag, bag 
         ^       ^
         bgbag,g    bgbag,g 
        
        """
        @lru_cache(None)
        def helper(i,j): 
            if j == len(t):
                return 1 
            elif i == len(s):
                return 0 
            
            res = 0 
            if s[i] == t[j]:
                res += helper(i + 1, j + 1) 
            res += helper(i + 1, j)
            
            return res 
        
        return helper(0,0)
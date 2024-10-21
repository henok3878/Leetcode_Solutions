class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        @cache 
        def helper(i, j):
            if j >= m:
                return i >= n # The only place we return True 

            if p[j] == '*':
                return (i < n and helper(i + 1, j)) or helper(i, j + 1) 
            elif i < n and (p[j] == '?' or (p[j] == s[i])):
                return helper(i + 1, j + 1) 
            return False 
        
        # return helper(0, 0)

        dp = [[False] * (m + 1) for _ in range( n + 1)] 
        #base case 
        dp[n][m] = True 
        for i in range(n,-1,-1):
            for j in range(m-1, -1, -1):
                if p[j] == '*':
                    if i < n:
                        dp[i][j] = dp[i + 1][j] 
                    dp[i][j] = dp[i][j] or dp[i][j + 1] 
                elif i < n and (p[j] == '?' or (p[j] == s[i])):
                    dp[i][j] = dp[i + 1][j + 1] 

        return dp[0][0]

        


            


"""
aa, *

- Branch 2 bayes for every *, use it and don't use it 

aaaaaaaaa....., 
*????????....

The worest case:

aaaaaaaa.....
 ^
********.....
^
worest case: 2^N, 

(i,j): unique combinations: n * n = N**2 


Number of redundant calls: (2^N - N^2)

With storage, we could reduce this time to O(N^2)

"""
class Solution:
    def uniquePaths(self, n: int, m: int) -> int:

        '''
        @cache
        def uniquePaths(i,j): # (i,j) represent curr cell 
            """
            returns the number ways to reach to the end(BR), from this cell. 
            """
            if i >= n or j >= m:
                return 0
            elif i == n-1 and m-1 == j:
                return 1
            
            down = uniquePaths(i + 1, j) 
            right = uniquePaths(i, j + 1) 

            return down + right 
        
        return uniquePaths(0,0)
        '''
        dp = [[0] * m for _ in range(n)]
        dp[n-1][m-1] = 1 # base case 
        for i in range(n-1, -1,-1):
            for j in range(m - 1, -1, -1):

                if i + 1 < n:
                    dp[i][j] += dp[i + 1][j] 
                if j + 1 < m:
                    dp[i][j] += dp[i][j + 1] 
        return dp[0][0]


    


"""
Step1: Restate the problem 
    ways to reach bottom-right starting from top-left moving either down or right.
Clarification: 
 - What would be the max size of the grid? 

 Appraoch 1: The straight forward way 
    - simulating the movment using recurssion. The state would i,j to reprsent the cell.
    - for each cell, we have two options;
        - either down or right and combine the result of two 
    - the time is exponential specfically 2**(n * m) 
    
Observation: even though the time is exponential (2**( n* m)), we actually have only n * m cells which are unique states (function calls). So, this tells if we memoize the result of each cell, 1. we avoid over counting 2. We avoid redundant calls. 

This reduces the time complexity to (n * m).

Bottom-UP:
- One observation from the top-down (recurssive + memoization) is we don't start building 
our result until we reach to the base case. We keep breaking down the problem till we reach there. The issue is we are wasting by going there because the actual work is being done we we get up from the base case. So, from this observation we can come up with bottom up appraoch. Which is a bit faster becuase it avoid going down and also we don't recurssive overhead. 


"""
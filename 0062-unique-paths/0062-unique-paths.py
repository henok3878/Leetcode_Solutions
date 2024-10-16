class Solution:
    def uniquePaths(self, n: int, m: int) -> int:

        @cache
        def uniquePaths(i,j): # (i,j) represent curr cell 
            '''
            returns the number ways to reach to the end(BR), from this cell. 
            '''
            if i >= n or j >= m:
                return 0
            elif i == n-1 and m-1 == j:
                return 1
            
            down = uniquePaths(i + 1, j) 
            right = uniquePaths(i, j + 1) 

            return down + right 
        
        return uniquePaths(0,0)
    


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


"""
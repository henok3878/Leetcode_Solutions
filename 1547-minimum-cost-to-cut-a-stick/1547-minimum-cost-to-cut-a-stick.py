class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        cuts.sort() 
        cuts.insert(0,0)
        cuts.append(n)
        
        N = len(cuts)
        dp  = [[float('inf')] * (N) for _ in range(N)]
                
        for i in range(N - 2, -1,-1):
            for j in range(1,N):
                if i + 1 >= j:
                    dp[i][j] = 0
                    continue 
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[k][j] +  dp[i][k], dp[i][j])
                    
                dp[i][j] += cuts[j] - cuts[i]
        return dp[0][N-1]
            
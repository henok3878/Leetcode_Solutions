class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        dp = [False] * (n + 1)  
        dp[1] = True
        
        for i in range(2, n + 1):
            for r in range(1, int(i ** 0.5) + 1):
                curr = r * r 
                if curr <= i:
                    if not dp[i-curr]:
                        dp[i] = True  
                else:
                    break 
        return dp[n]
        

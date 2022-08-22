class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        dp = [(False,True)] * (n + 1)  
        dp[1] = (True,False)
        
        for i in range(2, n + 1):
            for r in range(1, int(i ** 0.5) + 1):
                curr = r * r 
                if curr <= i:
                    if dp[i-curr][1]:
                        dp[i] = True,False    
                else:
                    break 
        return dp[n][0]
        

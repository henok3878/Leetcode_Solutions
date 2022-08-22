class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n < 2:
            return 1 
        dp = [0] * ( n + 1)  
        dp[1] = 1 
        dp[2] = 1 / n;
        
        for i in range(3,n + 1):
            dp[i] = dp[i - 1]
            dp[i] += dp[i-1]/ (n - (i - 2))
        return 1 - dp[n]
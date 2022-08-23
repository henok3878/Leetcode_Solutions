dp = defaultdict(lambda: -1) 
class Solution:
    
    def getKth(self, lo: int, hi: int, k: int) -> int: 
        global dp
        ans = []
        def find_steps(n):
            if n == 1:
                return 0 
            if dp[n] != -1:
                return dp[n] 
            dp[n] = 1 + find_steps(3*n + 1 if n % 2 != 0 else n // 2)
            return dp[n]
        
        
        for i in range(lo, hi + 1):
            ans.append((i,find_steps(i)))
        ans.sort(key = lambda item: (item[1], item[0]))
        return ans[k-1][0]
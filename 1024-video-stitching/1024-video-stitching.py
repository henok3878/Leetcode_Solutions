class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        
        N = len(clips)
        
        
        
        clips.sort() 
        if clips[0][0] > 0:
            return -1 
        dp = [[float('inf')] * (time + 1) for _ in range(N + 1)]
        for i in range(N + 1):
            dp[i][time] = 0 
        
        for i in range(N - 1, -1,-1):
            for c in range(time, -1,-1):
                if clips[i][0] <= c:
                    nxt = clips[i][1] if clips[i][1] <= time else time
                    dp[i][c] = 1 + dp[i + 1][nxt]
                
                dp[i][c] = min(dp[i][c], dp[i + 1][c])
        
        res = dp[0][0]
        return res if res != float('inf') else -1
    
    
    """
                            i,c     
        
    i + 1, clips[i][1]              i + 1, c 
    
    
    """
        
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        
        N = len(clips)
        
        @cache 
        def helper(idx, covered_sofar):
            if covered_sofar >= time:
                return 0 
            elif idx >= N:
                return float('inf')
            
            ret = float('inf') 
            if clips[idx][0] <= covered_sofar:
                ret = 1 + helper(idx + 1, clips[idx][1]) 
            
            return min(ret, helper(idx + 1, covered_sofar))
        
        clips.sort() 
        if clips[0][0] > 0:
            return -1 
        res = helper(0,0)
        
        return res if res != float('inf') else -1
        
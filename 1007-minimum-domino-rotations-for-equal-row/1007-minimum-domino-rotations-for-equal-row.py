class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        cand1, cand2 = tops[0], bottoms[0] 
        
        ans = float('inf')
        for cand in (cand1,cand2):
            count_top, count_bottom = 0, 0 
            flag = False 
            for i in range(len(tops)):
                if tops[i] != cand and bottoms[i] != cand:
                    flag = True 
                    break 
                if tops[i] == cand:
                    count_top += 1 
                if bottoms[i] == cand:
                    count_bottom += 1 
            if flag: continue 
            ans = min(ans,min(len(tops) - count_top, len(tops) - count_bottom)) 
        return ans if ans != float('inf') else -1
        
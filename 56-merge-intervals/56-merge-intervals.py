class Solution:
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        ans = []
        curr = intervals[0]
        for i in range(1,n):
            nxt = intervals[i]
            if(curr[1] >= nxt[0]):                
                curr[1] = max(nxt[1],curr[1])
            else:
                ans.append(curr[:])
                curr = nxt
        ans.append(curr)
        
        return ans
            
        
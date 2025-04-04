class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
       
        if not intervals:
            return [newInterval]
        newl, newr = newInterval 
        intervals.append([float('inf'), float('inf')])
        ans = [[-1,-1]] 
        n = len(intervals) 
        i = 0
        while i < n:
            l,r = intervals[i] 
            if (newl is not None) and l >= newl: 
                # insertion point 
                pl, pr = ans[-1] 
                if newl <= pr:
                    ans.pop()
                    newl = pl
                    newr = max(pr, newr)
                j = i + 1
                if l <= newr:
                    r = max(r, newr) 
                    while j < n and intervals[j][0] <= r:
                        r = max(r, intervals[j][1]) 
                        j += 1 
                    ans.append([newl, r])
                else:
                    ans.append([newl, newr])
                    ans.append([l, r]) 
                i = j 
                newl = None
            else:
                ans.append(intervals[i])  
                i += 1 
        return ans[1:-1]  
                
            
            



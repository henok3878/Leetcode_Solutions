class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = [] 
        intervals.sort() 
        intervals.append([float('inf'), float('inf')])
        curr_l, curr_r = intervals[0] 
        for l, r in intervals: 
            if l > curr_r: 
                ans.append([curr_l, curr_r]) 
                curr_l = l
            curr_r = max(curr_r, r)  
        return ans 
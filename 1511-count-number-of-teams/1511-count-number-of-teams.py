from sortedcontainers import SortedList
class Solution:
    def count_low_high(self,sl,x):
        lo = sl.bisect_left(x)
        hi = len(sl) - lo
        return lo, hi
    
    def numTeams(self, A):
        result = 0
        left   = SortedList()
        right  = SortedList(A)
        for x in A:
            right.remove(x)
            lo_L, hi_L  =  self.count_low_high(left ,x)
            lo_R, hi_R  =  self.count_low_high(right,x)
            result     +=  lo_L*hi_R + hi_L*lo_R
            left .add(x)
        return result
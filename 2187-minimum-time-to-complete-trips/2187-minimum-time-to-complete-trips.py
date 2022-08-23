class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        
        def possible(mid):
            trips = 0 
            for bus in time: 
                trips += (mid // bus)
            return trips >= totalTrips 
            
            
        lower, upper = 1, 10**14
        best = upper 
        while lower <= upper: 
            mid = lower + (upper - lower ) // 2 
            if possible(mid):
                best = mid 
                upper = mid - 1 
            else:
                lower = mid + 1 
        
        return best 
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
    
                
        def calc_diff_cw(x,y):
            return 60*(int(y[:2]) - int(x[:2])) + (int(y[3:]) - int(x[3:]))
        
        n = len(timePoints)
        timePoints.sort(key = lambda x: (int(x[:2]) * 60) + int(x[3:]))
        print(timePoints)
        
        min_cw = float("inf")
        for i in range(1,n):
            min_cw = min(min_cw, calc_diff_cw(timePoints[i-1], timePoints[i]))
    
        min_ccw = calc_diff_cw(timePoints[-1], "23:60") + calc_diff_cw("00:00",timePoints[0])  
        
        return min(min_ccw,min_cw)
import decimal 

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        n = len(stockPrices)
        if(n < 2):
            return 0
        if(n == 2):
            return 1
        
        stockPrices.sort()
        MAX = 10**20
        p_slope = MAX
        p_pt = stockPrices[0]
        line = 0;
        for i in range(1,n):
            x2,y2 = stockPrices[i]
            slope = decimal.Decimal(y2 - p_pt[1]) / decimal.Decimal(x2 - p_pt[0])
            if slope != p_slope:
                line += 1;
                p_slope = slope 
            p_pt = (x2,y2)
            
        return line
            
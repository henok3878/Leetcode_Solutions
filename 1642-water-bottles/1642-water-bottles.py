class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        empty = 0 
        while numBottles > 0 or empty >= numExchange: 
            ans += numBottles 
            temp = numBottles 
            numBottles = ( empty + numBottles) // numExchange 
            empty = ((empty + temp) % numExchange)
        return ans 
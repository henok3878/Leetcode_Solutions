class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        ans = 1 
        delta = 1
        for i in range(time):
            ans += delta 
            if(ans == n):
                delta = -1 
            elif(ans == 1):
                delta = 1 
        return ans 
            
        
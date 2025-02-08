class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = 0 
        t = abs(x)
        while t: 
            d = t % 10 
            t //= 10 
            y = y*10 +  d 
        return x == y 

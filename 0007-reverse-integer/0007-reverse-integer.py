class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2 ** 31 
        MAX = 2**31 - 1 
        rev = 0 
        sign = -1 if x < 0 else 1 
        x = abs(x)
        while x: 
            rev *= 10 
            rev += ( x % 10) 
            x //= 10 
        
        rev *= sign 
        return 0 if rev < MIN or rev > MAX else rev 
        
        
        
        
        
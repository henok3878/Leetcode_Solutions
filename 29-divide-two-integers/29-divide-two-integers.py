class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg=( (dividend < 0) != (divisor < 0) )
        dividend = left = abs(dividend)
        divisor  = div  = abs(divisor)
        Q = 1
        ans = 0
        while left >= divisor:
            left -= div
            ans  += Q 
            Q    += Q
            div  += div
            if left < div:
                div = divisor
                Q = 1
        if neg:
            return max(-ans, -2147483648)
        else:
            return min(ans, 2147483647)
    """
        0011
    1010 -> 0011
    (10) -> (3)
    
    1010 -> 
    
    x/y => x/ (2*y/2) => (x/2)/(y/2) => 
    
    
    0011 -> 0010 and 0001 
    
    1010/0010 => shift to right 1 times: => 0101 
    
    
    """
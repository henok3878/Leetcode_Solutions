class Solution:
    def minNumberOfSeconds(self, x: int, w: List[int]) -> int:
        low = 0
        mx_time = max(w) 
        high = mx_time * (x * (x + 1) // 2) 
        while low < high:
            mid = (low + high) // 2
            total = 0
            for wt in w:
                s = mid // wt  
                d =  s * 8 + 1
                sq = math.isqrt(d)  
                curr = (sq - 1) // 2
                while curr > 0 and curr * (curr + 1) // 2 > s:
                    curr -= 1
                total += curr
            if total >= x: 
                high = mid
            else:
                low = mid + 1
        return low

'''
4
[ 2, 1, 1]  

x *(x + 1) // 2 : arth sum 

Binary search + isPos condition 

'''
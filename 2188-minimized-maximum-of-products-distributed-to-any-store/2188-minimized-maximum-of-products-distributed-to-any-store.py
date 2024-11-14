class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        def is_pos(x):
            stores = 0 
            for q in quantities:
                stores += (q + (x - 1)) // x
            return stores <= n 

        low = 1 
        high = 10**10 
        best = high
        while low <= high:
            mid = (low + high) // 2 
            if(is_pos(mid)):
                best = mid 
                high = mid - 1 
            else:
                low = mid + 1 
        return best 


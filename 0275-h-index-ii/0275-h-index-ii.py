class Solution:
    def hIndex(self, citations: List[int]) -> int:
        best = 0 
        low = 0
        high = 10**3 

        def pos(x):
            cnt = 0 
            for num in citations:
                if num >= x:
                    cnt += 1 
            return cnt >= x 
        while low <= high:
            mid = (low + high) // 2 
            if pos(mid):
                best = mid 
                low = mid + 1 
            else:
                high = mid - 1 
        return best 
            
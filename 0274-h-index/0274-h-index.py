class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        def isPos(x):
            cnt = 0 
            for c in citations:
                if c >= x:
                    cnt += 1
            return cnt >= x 
        ans = 0 
        l = 0 
        h = n 
        while l <= h:
            mid = (l + h) // 2 
            if isPos(mid):
                l = mid + 1 
                ans = mid 
            else:
                h = mid - 1 
        return ans 
        
        
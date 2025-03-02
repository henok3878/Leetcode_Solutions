class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True) 
        ans = 0
        for i, cite in enumerate(citations):
            if cite >= (i + 1):
                ans = max(ans,i + 1) 
        return ans 
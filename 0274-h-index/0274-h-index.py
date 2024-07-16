class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        cands = [0] * (n + 1) 
        for c in citations:
            if c > n:
               c = n 
            cands[c] += 1 

        suffix = 0 
        for i in range(n,-1,-1):
            suffix += cands[i]
            if suffix >= i:
                return i 
        return 0
        
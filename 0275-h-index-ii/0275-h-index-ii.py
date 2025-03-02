class Solution:
    def hIndex(self, citations: List[int]) -> int:
        mx = max(citations) 
        n = len(citations)
        counts = [0] * (mx + 1) 
        for cite in citations:
            counts[cite] += 1 
        sorted_citations = [] 
        for i, cnt in enumerate(counts):
            if cnt:
                for _ in range(cnt):
                    sorted_citations.append(i) 
        # print(sorted_citations)
        for i in range(n):
            rem = (n - i) 
            if sorted_citations[i] >= rem:
                return rem 
        return 0 
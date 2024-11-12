class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort() 
        queries = [(q, i) for i,q in enumerate(queries)]
        queries.sort() 
        ans = [0] * len(queries) 
        best = 0
        i = 0 
        for q, q_i in queries:
            while i < len(items) and items[i][0] <= q:
                best = max(items[i][1], best) 
                i += 1 
            ans[q_i] = best
        return ans
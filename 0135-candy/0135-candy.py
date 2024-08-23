class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        lr = [0] * n 
        p = float('inf') 
        incr = 0 
        for i in range(n):
            if ratings[i] > p:
                incr += 1 
            else:
                incr = 0
            p = ratings[i] 
            lr[i] = incr 
        incr = 0 
        p = float('inf')
        ans = 0
        for i in range(n-1,-1,-1):
            if ratings[i] > p:
                incr += 1 
            else:
                incr = 0 
            p = ratings[i]
            curr = max(lr[i], incr) 
            ans += (curr + 1) 
        return ans
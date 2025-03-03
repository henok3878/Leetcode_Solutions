class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        lr = [0] * n 
        lr[0] = 1  
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                lr[i] = lr[i-1] + 1 
            else:
                lr[i] = 1 
        rl = 1 
        lr[-1] = max(lr[-1], 1) 
        for i in range(n-2, -1,-1):
            if ratings[i] > ratings[i + 1]:
                rl += 1   
            else:
                rl = 1
            lr[i] = max(lr[i], rl)
        return sum(lr)
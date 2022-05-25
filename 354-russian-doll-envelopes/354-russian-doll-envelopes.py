class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        if n == 1:
            return n
        """
            Find the longest increasing envelopes 
        
        """  
        envelopes.sort(key=lambda  x: (x[0], -x[1]))
        dp = [None] * n
        tails=[]
        
        for (w,h) in envelopes:
            idx= bisect.bisect_left(tails, h)
            if idx==len(tails):
                tails.append(h)                        
            elif idx==0 or tails[idx-1]<h:
                tails[idx]=h
        return len(tails) 
        
        """
        [[2, 100], [3, 200], [4, 300], [5, 250], [5, 400], [5, 500], [6, 360], [6, 370], [7, 380]]

            0           1       2        3          4          5        6           7       8 
        
        """
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        n = len(tickets)
        kth = tickets[k]
        
        for i,tic in enumerate(tickets):
            if i > k:
                if tic >= kth:
                    time += kth - 1
                else:
                    time += tic
            else:
                time += min(kth,tic)
            
        return time
                
            
        
        """
        1,3,2
        1 + 2 + 2 = 5
        [84,49,5,24,70,77,87,8]
                  3
                  
        24 + 24 + 5 + 24 + 24 + 24 + 24 + 8 
        
        24
        *6 
        144 + 13
        157
        """
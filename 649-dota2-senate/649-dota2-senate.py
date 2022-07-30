class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        r_banned = 0 
        d_banned = 0 
        r_count = senate.count('R')
        d_count = senate.count('D')
        
        senate = list(senate)
        while r_count > 0 and d_count > 0: 
            for i,s in enumerate(senate): 
                if s == 'R':
                    if r_banned > 0: 
                        senate[i] = " "
                        r_banned -= 1 
                        r_count -= 1 
                    else:
                        d_banned += 1 
                elif s == 'D':
                    if d_banned > 0:
                        senate[i] = " "
                        d_count -= 1 
                        d_banned -= 1 
                    else: 
                        r_banned += 1
                        
        if r_count: 
            return "Radiant" 
        else:
            return "Dire"
            
                
        
        """
        
        Rights: 
            -> Ban one (Remove elem) 
            -> Announce 
        """
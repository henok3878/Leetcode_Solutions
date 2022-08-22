class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        """
        (i):
            if i == 1:
                return (True, False) 
            elif i <= 0:
                return (False, True)
            res = False, True 
            for r in range(1, sqrt(i)):
                curr = r * r 
                if curr <= i:
                    next_res = (i - curr)
                    if next_res[1]:
                       res = True, False             
        
        """
        
        @cache 
        def play(i):
            if i == 1:
                return True, False 
            elif i <= 0:
                return False, True 
            
            res = False, True 
            for r in range(1, int(i ** 0.5) + 1):
                curr = r * r 
                if curr <= i:
                    next_game = play(i - curr) 
                    if next_game[1]:
                        res = True, False 
                        break 
            return res
        
        return play(n)[0]
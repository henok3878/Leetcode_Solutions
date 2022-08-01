class Solution:
    def divisorGame(self, n: int) -> bool:
        
        @cache 
        def helper(n):
            if n == 1:
                return False 
            elif n == 2:
                return True 
            op1 = False 
            for i in range(1,n):
                if n % i == 0:
                    op1 = op1 or not helper(n - i)
            return op1 

        return helper(n)
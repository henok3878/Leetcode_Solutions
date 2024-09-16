class Solution:
    def isHappy(self, n: int) -> bool:
        cache = {} 
        seen = set()
        def helper(x):
            if x == 1:
                return True 
            elif x in cache:
                return cache[x]
            elif x in seen or x == 0:
                return False 
            seen.add(x)
            nxt = 0 
            temp = x 
            while temp:
                nxt += ((temp % 10) ** 2) 
                temp //= 10

            cache[x] = helper(nxt)
            return cache[x]

        return helper(n)
            
        
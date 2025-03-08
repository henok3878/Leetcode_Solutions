class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        mod = int(1e9) + 7
        p = 31 
        inv_p = pow(p, mod - 2, mod) 

        n = len(haystack)
        m = len(needle)
        if n < m:
            return -1 
            
        def idx(ch):
            return ord(ch) - ord('a') 
        

        def hash(word):
            val = 0
            pol = 1
            for ch in word:
                ch_num = idx(ch) 
                val = (val + (ch_num * pol) % mod ) % mod 
                pol = (pol * p) % mod 
            return val 

        def check(st):
            for i in range(m):
                if needle[i] != haystack[i + st]:
                    return False 
            return True 

        req = hash(needle) 
        curr = 0
        pol = 1 
        for i in range(m):
            ch_num = idx(haystack[i])
            curr = (curr + (ch_num * pol) % mod) % mod 
            pol = (pol * p) % mod 
        
        if curr == req and check(0):
            return 0  
        pol = (pol * inv_p) % mod 
        for i in range(m, n):
            curr = (curr - idx(haystack[i-m])) % mod 
            curr = (curr * inv_p) % mod 
            curr = (curr + (pol * idx(haystack[i])) % mod) % mod 
            if curr == req and check(i - m + 1): 
                return i - m + 1 
        return -1 
         

            
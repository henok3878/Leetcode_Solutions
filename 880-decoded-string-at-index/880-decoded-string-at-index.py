class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        total_len = 0
        for c in s:
            if c.isdigit():
                total_len *= int(c) 
            else:
                total_len += 1 
        n = len(s)
        for i in range(n-1,-1,-1):
            c = s[i] 
            k %= total_len 
            if c.isdigit():
                total_len //= int(c) 
            else:
                if k == 0:
                    return c 
                else:
                    total_len -= 1 
                    
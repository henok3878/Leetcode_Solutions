class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        k -= 1 
        total_len = 0
        for c in s:
            if c.isdigit():
                total_len *= int(c) 
            else:
                total_len += 1 
        n = len(s)
        for i in range(n-1,-1,-1):
            c = s[i] 
            if c.isdigit():
                total_len //= int(c) 
                if k + 1 > total_len:
                    k %= total_len 
            else:
                if k + 1 == total_len:
                    return c 
                else:
                    total_len -= 1 
                    
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        result = ord(columnTitle[-1]) - ord('A') + 1
        if n == 1:
            return result 
        for i in range(1,n):
            result += (26 ** i) 
        
        for i in range(n-1):
            result += (ord(columnTitle[i]) - ord('A'))*(26**(n-i - 1))
        return result
        
    
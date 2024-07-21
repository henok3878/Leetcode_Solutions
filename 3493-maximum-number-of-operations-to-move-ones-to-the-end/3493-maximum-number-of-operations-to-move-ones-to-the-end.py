class Solution:
    def maxOperations(self, s: str) -> int:
        ones = 0
        ans = 0
        prev = '-'
        for c in s:
            if c == '1':
                ones += 1
            elif prev != '0':
                ans += ones 
            prev = c 
        return ans 
                
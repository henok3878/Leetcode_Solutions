class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0 
        curr = 0
        for i in range(len(s)):
            if s[i] == ' ':
                curr = 0 
            else:
                curr += 1
                ans = curr
        return ans
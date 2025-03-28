class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_i = {} 
        n = len(s)
        left = -1
        ans = 0 
        for i in range(n):
            if s[i] in last_i and last_i[s[i]] > left:
                left = last_i[s[i]] 
            last_i[s[i]] = i 
            ans = max(ans, i - left)
        return ans 
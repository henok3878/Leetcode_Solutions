class Solution:
    def romanToInt(self, s: str) -> int:
        mappings = {"I": 1, "V": 5, "X": 10, "L": 50,  "C": 100,  "D": 500, "M": 1000}
        ans = 0
        n = len(s) 
        st = 0 
        while st < n:
            val1 = mappings[s[st]] 
            if st + 1 < n and mappings[s[st + 1]] > val1:
                ans += (mappings[s[st + 1]] - val1) 
                st += 1 
            else:
                ans += val1 
            st += 1 
        return ans 
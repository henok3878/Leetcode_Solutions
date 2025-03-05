class Solution:
    def romanToInt(self, s: str) -> int:
        mappings = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, 
            "XC": 90, "C": 100, "CD": 400,  "D": 500,"CM": 900, "M": 1000}
        ans = 0
        n = len(s) 
        st = 0
        for k in reversed(mappings.keys()):
            len_k = len(k) 
            if st >= n:
                break 
            while st + len_k <= n and s[st: st + len_k] == k:
                ans += mappings[k] 
                st += len_k
        return ans 
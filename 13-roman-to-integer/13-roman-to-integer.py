class Solution:
    def romanToInt(self, s: str) -> int:
        
        mapping = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M" : 1000}
        n = len(s)
        result = 0
        i = 0
        while i < n-1:
            if mapping[s[i]] >= mapping[s[i + 1]]:
                result += mapping[s[i]]
                i += 1
            else:
                result += mapping[s[i + 1]] - mapping[s[i]]
                i += 2 
        result += mapping[s[n-1]] if n == 1 or mapping[s[n-2]] >= mapping[s[n-1]] else 0
        return result
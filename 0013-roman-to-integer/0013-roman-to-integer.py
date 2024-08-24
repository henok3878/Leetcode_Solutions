class Solution:
    def romanToInt(self, s: str) -> int:
        symbols_int = {"I": 1, "V": 5, "X" : 10, "L": 50, "C" : 100, "D" : 500, "M" : 1000} 
        n = len(s) 
        total = 0
        i = 0
        while i < n:
            curr = symbols_int[s[i]]
            if i < (n - 1) and symbols_int[s[i + 1]] > curr: 
                total += (symbols_int[s[i + 1]] - curr) 
                # print(symbols_int[s[i + 1]] - curr)
                i += 1
            else:
                total += curr
                # print(curr)
            i += 1
        return total 
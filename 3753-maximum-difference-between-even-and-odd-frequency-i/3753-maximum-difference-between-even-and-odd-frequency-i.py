class Solution:
    def maxDifference(self, s: str) -> int:
        freqs = [-1] * 26 
        for c in s:
            idx = ord(c) - ord('a') 
            if freqs[idx] == -1:
                freqs[idx] = 0 
            freqs[idx]  += 1 

        odd = max(num for num in freqs if num % 2) 
        even = min(num for num in freqs if num % 2 == 0) 
        
        return odd - even 
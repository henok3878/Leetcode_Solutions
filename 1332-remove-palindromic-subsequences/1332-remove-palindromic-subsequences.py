class Solution:
    def removePalindromeSub(self, s: str) -> int:
        
        def isPali(s):
            i = 0 
            j = len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                else:
                    i += 1
                    j -= 1
            return True
        if isPali(s):
            return 1
        return 2
        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        len(words) = 1000 
        len(words[i]) = 20 
        '''
        words = set(wordDict) 
        n = len(s)
        @cache
        def helper(i):
            if i == n:
                return True 
            else:
                res = False
                for j in range(i, n):
                    word = s[i:j + 1] 
                    if word in words:
                        res = res or helper(j + 1)
                return res 
        return helper(0)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        len(words) = 1000 
        len(words[i]) = 20 
        '''
        words = set(wordDict) 
        n = len(s)
        @cache
        def helper(curr_s):
            if curr_s == "":
                return True 
            else:
                res = False
                for i in range(len(curr_s)):
                    word = curr_s[:i + 1] 
                    if word in words:
                        res = res or helper(curr_s[i + 1: ])
                return res 
        return helper(s)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        
        Minumum: 
        
        Thinking what not to touch in word1: Don't touch longest common subsequence 
        
        "horse", "ros"
        
        LCS = rs 
        
        - len(word1) - len(word2) delations is needed 
        - len(word2) - len(lcs): replacment 
        
        Won't work: 
            -> ex: orse , ros 
                - lcs = rs 
                - ors
                        
        h o r s e
            
        - - -  , r and s are selected and 2 delations performed 
        
        
        h o r s e,  r o s 
        ^           ^ 
        
        if word1[i] != word2[j]:
            # match them by replacing or inserting or deleting 
        
        else: 
            # curr char matched 
            word1[i + 1], word2[i + 1]
        
        
        
        """
        
        
        @cache 
        def helper(i,j):

            if j == len(word2):
                return len(word1) - i 
            elif i == len(word1):
                return len(word2) - j
            
            res = float('inf')
            if word1[i] == word2[j]:
                res = min (res, helper( i + 1, j + 1) ) 
            else:
                res = min(helper(i,j + 1), helper(i + 1, j), helper(i + 1, j + 1)) + 1
            
            return res 
        
        return helper(0,0)
            
        
        
        
        
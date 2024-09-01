class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mappings = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6': 'mno', '7':'pqrs', '8':'tuv','9':'wxyz'} 
        ans = []
        n = len(digits)
        def helper(i, curr):
            if i >= n:
                if curr:
                    ans.append(curr) 
                return
            for c in mappings[digits[i]]:
                helper(i + 1, curr + c) 
        
        helper(0,'')
        return ans 


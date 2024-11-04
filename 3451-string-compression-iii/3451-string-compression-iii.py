class Solution:
    def compressedString(self, word: str) -> str:
        res = "" 
        curr = ''
        word += '*'
        for c in word:
            if not curr or (curr[0] == c and len(curr) < 9):
                curr += c
            else:   
                res += f"{len(curr)}{curr[0]}" 
                curr = c
        return res
            
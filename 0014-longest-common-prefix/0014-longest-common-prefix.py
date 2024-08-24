class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cnt = 0 
        for i in range(len(strs[0])):
            curr = strs[0][i]
            for s in strs:
                if i >= len(s) or (curr != s[i]):
                    return strs[0][:cnt]
            cnt += 1 
        return strs[0][:cnt]
                    
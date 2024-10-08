class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort() 
        first = strs[0] 
        last = strs[-1] 
        cnt = -1
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                cnt = i
            else:
                break 
        return first[:cnt + 1]
        
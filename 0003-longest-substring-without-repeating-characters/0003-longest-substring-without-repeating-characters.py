class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        l = r = 0 
        n = len(s)
        ans = 0
        for i,c in enumerate(s):
            if c in used:
                ans = max(ans, i - l) 
                cIdx = used[c] 
                while l <= cIdx:
                    del used[s[l]]
                    l += 1 
            
            used[c] = i
        ans = max(ans, len(used))
        return ans
                    



                
                
                

                
        
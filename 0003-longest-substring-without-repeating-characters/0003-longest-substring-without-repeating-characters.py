class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        l = 0
        n = len(s)
        ans = 0
        for i,c in enumerate(s):
            if c in used and used[c]  >= l:
                cIdx = used[c] 
                l = cIdx + 1
            ans = max(ans, i - l + 1) 
            used[c] = i
        
        return ans
                    



                
                
                

                
        
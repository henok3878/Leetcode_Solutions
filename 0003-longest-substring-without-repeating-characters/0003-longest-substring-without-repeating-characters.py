class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        n = len(s)
        ans = 0
        for i,c in enumerate(s):
            while c in seen:
                seen.remove(s[l]) 
                l += 1 
            seen.add(c)
            ans = max(ans, i - l + 1) 
        
        return ans
                    



                
                
                

                
        
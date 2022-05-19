class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        ans = (0,0)
        size = 0
        n = len(s)
        # for odd case 
        for i in range(n):
            l ,r = i,i
            while(l >= 0 and r < n and s[l] == s[r]):
                if r - l + 1 > size:
                    ans = (l,r)
                    size = r - l + 1
                l -= 1
                r += 1     
        
        # for even case 
        for i in range(n):
            l ,r = i - 1,i
            while(l >= 0 and r < n and s[l] == s[r]):
                if r - l + 1 > size:
                    ans = (l,r)
                    size = r - l + 1
                l -= 1
                r += 1    
        
        return s[ans[0]: ans[1] + 1]

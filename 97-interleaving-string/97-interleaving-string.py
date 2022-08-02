class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
       
    
        len1 = len(s1) 
        len2 = len(s2) 
        len3 = len(s3)
        
        @cache 
        def helper(l1, l2, i):
            
            if i >= len3 and l1 >= len1 and l2 >= len2: 
                return True 
            elif i >= len3 or (l1 >= len1 and l2 >= len2):
                return False
            
            res = False 
            if l1 < len1 and  s1[l1] == s3[i]:
                res = res or helper(l1 + 1, l2, i + 1) 
            
            if l2 < len2 and s2[l2] == s3[i]:
                res = res or helper(l1, l2 + 1, i + 1) 
            
            return res 
        
        return helper(0,0,0)
            
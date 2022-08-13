class Solution:
    def minInsertions(self, s: str) -> int:
        
        
        @cache 
        def find_longest(i,j):
            
            if i == j:
                return 1 
            elif i > j:
                return 0 
            elif s[i] == s[j]:
                return 2 + find_longest(i + 1, j - 1) 
            else:
                return max(find_longest(i + 1, j), find_longest(i,j - 1)) 
            
        longest = find_longest(0, len(s) - 1) 
        
        return len(s) - longest 
            
            
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        @cache 
        def helper(i, j):
            if j >= m:
                return i >= n
            
            
            if p[j] == '*':
                return (i < n and helper(i + 1, j)) or helper(i, j + 1) 
            elif i < n and (p[j] == '?' or (p[j] == s[i])):
                return helper(i + 1, j + 1) 
            return False 
        
        return helper(0, 0)
            


"""
aa, *

- Branch 2 bayes for every *, use it and don't use it 

aaaaaaaaa....., 
*????????....

The worest case:

aaaaaaaa.....
 ^
********.....
^
worest case: 2^N, 

(i,j): unique combinations: n * n = N**2 


Number of redundant calls: (2^N - N^2)

With storage, we could reduce this time to O(N^2)

"""
class Solution:
    def minimumTotal(self, t: List[List[int]]) -> int:
        @lru_cache
        def helper(i, j):
            if i == len(t)-1:
                return t[i][j]
            
            return t[i][j] + min(helper(i+1, j), helper(i+1, j+1))
                              
        return helper(0, 0)

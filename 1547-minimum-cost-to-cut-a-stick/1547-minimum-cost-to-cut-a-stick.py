class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        cuts.sort() 
        cuts.insert(0,0)
        cuts.append(n)
        
        @cache 
        def helper(i,j):
            if i + 1 >= j:
                return 0
            
            cost = float('inf')
            for k in range(i + 1, j):
                 cost = min(helper(k,j) + helper(i,k) , cost)        
            return cost + (cuts[j] - cuts[i])
        
        return helper(0,len(cuts) - 1)
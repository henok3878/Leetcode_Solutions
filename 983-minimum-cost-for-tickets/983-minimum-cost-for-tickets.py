class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        
        n = len(days)
        MAX = 10**20
        ways = {0:0,1:6,2:29}
        
        @cache
        def helper(idx,avail):
            if idx == n:
                return 0
            
            res = MAX
            if days[idx] <= avail:
                res = helper(idx + 1, avail)
            else:
                for i,c in enumerate(costs):
                    res = min(res,c + helper(idx + 1, days[idx] + ways[i]))
            return res
        
        return helper(0,0)
        """
        BruteForce: 
            days = [1,4,6,7,8,20], costs = [2,7,15]
                          
            [4,6,7,8,20],1      [4,6,7,8,20],7         [4,6,7,8,30] 15

            total sub problems: 3^365
        """
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}

        def helper(idx):
            if idx >= n:
                return 0
            if idx in memo:
                return memo[idx]
                
            curr_cost = cost[idx] 
            future_cost = min(helper(idx + 1), helper(idx + 2))
            total_cost = curr_cost + future_cost 
            memo[idx] = total_cost 

            return total_cost 

        return min(helper(0), helper(1))

    

'''
for each index, explore both cases (climb one stair & climbing two stairs)

    1 -> [2, 3] -> [3, 4 | 4, 5] -> [4, 5 | 5 , 6 | 5, 6 | 6 , 7]
    2**0  2**1         2 ** 2.             2 ** 3 

    Unique indeces: n

    total nodes: 2 ** n 
'''
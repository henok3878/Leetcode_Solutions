class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        memo[n] = 0
        memo[n + 1] = 0
        for i in range(n - 1, -1,-1):
            memo[i] = min(memo[i + 1], memo[i + 2]) + cost[i]
        return min(memo[0], memo[1])

    

'''
for each index, explore both cases (climb one stair & climbing two stairs)

    1 -> [2, 3] -> [3, 4 | 4, 5] -> [4, 5 | 5 , 6 | 5, 6 | 6 , 7]
    2**0  2**1         2 ** 2.             2 ** 3 

    Unique indeces: n

    total nodes: 2 ** n 

-----> go down (This is just calling smaller subproblems)
<----- go up (This is where we actually do the work)

0 -> [1, 2] 
1 -> [2, 3] -
'''

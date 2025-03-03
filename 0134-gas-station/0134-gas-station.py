class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        st = 0
        curr = 0
        for j in range(2*n):
            i = j % n
            curr += gas[i] - cost[i]
            if curr < 0:
                curr = 0
                st = j + 1
            if j - st + 1 >= n:
                return st 
        return -1 
            



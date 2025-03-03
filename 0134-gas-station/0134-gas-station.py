class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        delta = [gas[i] - cost[i] for i in range(n)] 
        delta += delta 
        curr = 0 
        i = 0
        j = 0 
        while i < n and j < len(delta):
            curr += delta[j] 
            while curr < 0 and i <= j:
                curr -= delta[i] 
                i += 1 
            j += 1 
            if curr >= 0 and j - i >= n:
                return i
        return -1 


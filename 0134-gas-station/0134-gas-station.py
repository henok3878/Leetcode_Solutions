class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
            -------------------->
                        --------> 
            ------------>
        '''
        n = len(gas)
        deltas = [ (x - y) for x,y in zip(gas, cost)]
        total = sum(deltas) 
        if total < 0:
            return -1 
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + deltas[i]
        mx = float('-inf') 
        idx = -1 
        for i in range(n):
            right = prefix[-1] - prefix[i] 
            # print('I: ', i, "right: ", right)
            if right > mx:
                idx = i 
                mx = right 
        return idx
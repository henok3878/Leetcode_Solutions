class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
            -------------------->
                        --------> 
            ------------>
        '''
        n = len(gas)
        deltas = [ (x - y) for x,y in zip(gas, cost)]
        total = 0 
        curr_delta = 0
        ans = 0
        for i,val in enumerate(deltas):
            total += val 
            curr_delta += val 
            if curr_delta < 0:
                ans = i + 1
                curr_delta = 0 
        return -1 if total < 0 else ans

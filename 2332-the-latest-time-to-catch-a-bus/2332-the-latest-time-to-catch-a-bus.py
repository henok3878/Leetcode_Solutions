class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort() 
        passengers.sort() 
        
        i = 0 
        for dprt in buses:
            curr = capacity 
            while curr > 0 and i < len(passengers) and  passengers[i] <= dprt:
                curr -= 1 
                i += 1
            if curr == 0:
                best = passengers[i-1]
            else:
                best = dprt 
        set_p = set(passengers) 
        while best in set_p:
            best -= 1 
        return best 
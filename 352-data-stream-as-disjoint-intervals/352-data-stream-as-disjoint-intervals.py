from sortedcontainers import SortedList 

class SummaryRanges:

    def __init__(self):
        self.list = SortedList([[float('-inf'),float('-inf')], [float('inf'),float('inf')]]) 

    def addNum(self, val: int) -> None:
        idx = self.list.bisect_left([val,val]) 

        prev = self.list[idx - 1]
        nxt = self.list[idx] 
        if prev[1] == val - 1 and nxt[0] == val + 1:
            prev[1] = nxt[1]
            self.list.pop(idx)
        elif prev[1] >= val - 1: 
            prev[1] = max(val,prev[1]) 
        elif nxt[0] == val or nxt[0] == val + 1:
            nxt[0] = min(val, nxt[0])
        else:
            self.list.add([val,val])
        

    def getIntervals(self) -> List[List[int]]:
        return self.list[1:-1]        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
from sortedcontainers import SortedList 

class MyCalendarThree:

    def __init__(self):
        self.events = SortedList()
        

    def book(self, start: int, end: int) -> int:
        self.events.add((start, 1)) 
        self.events.add((end, -1)) 
        ans = 0 
        count = 0 
        for st,v in self.events:
            count += v 
            ans = max(ans,count)
        return ans 


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
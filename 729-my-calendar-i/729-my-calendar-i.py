
from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        self.books = SortedList() 

    def book(self, start: int, end: int) -> bool:
        
        idx = self.books.bisect_left((start,end))
        st_prev, end_prev = self.books[idx - 1] if idx > 0 else (-1,-1) 
        st_next, end_next = self.books[idx] if idx < len(self.books) else  (float('inf'),float('inf'))
        if start < end_prev or end > st_next:
            return False 
        self.books.add((start,end))
        return True 


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

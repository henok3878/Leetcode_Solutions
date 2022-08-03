
from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        self.books = SortedList() 

    def book(self, start: int, end: int) -> bool:
        
        idx = self.books.bisect_left((start,end))
        #print(self.books,start,end, idx)
        if idx == len(self.books):
            st_prev, end_prev = self.books[idx - 1] if idx > 0 else (-1,-1) 
            #print("idx == len", st_prev, end_prev,start,end)
            if start < end_prev: 
                return False 
        else:
            
            st_prev, end_prev = self.books[idx - 1] if idx > 0 else (-1,-1) 
            st_next, end_next = self.books[idx] 
            #print(st_prev,end_prev, st_next, end_next)
            if start < end_prev or end > st_next:
                return False 
        self.books.add((start,end))
        return True 


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)



"""

[10,20], [15,25] , [20,30] 


[st1 , end1) 

[st2, end2)

"""
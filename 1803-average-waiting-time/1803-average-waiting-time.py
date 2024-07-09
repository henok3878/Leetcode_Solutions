class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        finish = 0 
        total_waiting = 0
        for a,t in customers:
            st = max(finish, a)
            finish = st + t
            total_waiting += finish - a
        return total_waiting / len(customers)
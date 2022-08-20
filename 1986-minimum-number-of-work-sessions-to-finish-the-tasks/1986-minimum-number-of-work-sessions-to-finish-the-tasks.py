class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        
        
        def is_possible(idx):
            if idx == n:
                return True 
            
            for i in range(mid):
                if slots[i] - tasks[idx] < 0:
                    continue 
                slots[i] -= tasks[idx]
                if is_possible(idx + 1):
                    return True 
                slots[i] += tasks[idx] 
                if slots[i] == sessionTime:
                    break 
            return False 
            
            
        n = len(tasks) 
        tasks.sort(reverse = True) 
        l,r = 1, n 
        ans = n 
        while l <= r:
            mid = (l + r) // 2 
            #print(l,r,mid)
            slots = [sessionTime] * mid 
            if is_possible(0):
                r = mid - 1
                ans = mid 
            else:
                l = mid + 1 
        return l 
    
    
    """    
    
    """
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        mxDist = -1 
        mnDist = float('inf') 
        
        first_critical = -1 

        curr_idx = 1 # curr node index 
        prev_critical_idx = -1 # prev critical point index 

        prev = head 
        curr = head.next 
        while(curr.next != None):
            nxt = curr.next 
            if (prev.val < curr.val > nxt.val ) or (prev.val > curr.val < nxt.val):
                # critical point 
                if(first_critical == -1):
                    first_critical = curr_idx
                else: 
                    mnDist = min(mnDist, curr_idx - prev_critical_idx)
                prev_critical_idx = curr_idx 
            
            curr_idx += 1 
            prev = curr 
            curr = nxt 
        
        if(first_critical != -1 and (prev_critical_idx > first_critical)):
            mxDist = (prev_critical_idx - first_critical)

        if mnDist == float('inf'):
            mnDist = -1 

        return [mnDist, mxDist]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy =  ListNode(-1,head) 
        temp = dummy
        nxt = head 
        swaps = (right - left)
        for _ in range(left-1):
            temp = temp.next

        prev = temp.next
        curr = temp.next.next 
       
        while(swaps > 0):
            nxt = curr.next 
            curr.next = prev 
            prev = curr 
            curr = nxt 
            swaps -= 1
        temp.next.next = curr
        temp.next = prev

        return dummy.next 
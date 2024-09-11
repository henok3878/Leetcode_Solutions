# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1,head)
        left = dummy
        right = dummy
        while n:
            right = right.next 
            n -= 1
        while right and right.next:
            left = left.next 
            right = right.next
        left.next = left.next.next if left.next else None 
        return dummy.next 
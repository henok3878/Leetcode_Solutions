# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        tail = dummy_head
        carry = 0 
        while l1 or l2 or carry > 0:
            curr_sum = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0) 
            carry = curr_sum // 10
            curr_node = ListNode(curr_sum % 10) 
            tail.next = curr_node 
            tail = curr_node 
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None 
        
        return dummy_head.next 
            

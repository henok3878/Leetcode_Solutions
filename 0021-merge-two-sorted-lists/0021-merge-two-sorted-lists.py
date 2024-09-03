# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode() 
        tail = dummy_head 
        while list1 or list2:
            new_node = list1 if not list2 else list2
            if list1 and list2:
                new_node = list1 if (list1.val <= list2.val) else list2 
            tail.next = new_node 
            tail = new_node
            list1 = list1.next if tail == list1 else list1
            list2 = list2.next if tail == list2 else list2
        return dummy_head.next 
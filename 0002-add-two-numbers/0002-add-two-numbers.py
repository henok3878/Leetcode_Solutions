# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = l1 
        num2 = l2 
        carry = 0 
        temp = ListNode() 
        dummy = temp  
        while num1 or num2 or carry:
            curr = carry 
            
            if num1: 
                curr += num1.val 
                num1 = num1.next 
            if num2:
                curr += num2.val 
                num2 = num2.next 

            carry = curr // 10 
            curr %= 10  

            temp.next = ListNode(val = curr) 
            temp = temp.next 

        return dummy.next 
"""
9,9,9,9,9,9,9
9 9 9 9 0 0 0 

""" 
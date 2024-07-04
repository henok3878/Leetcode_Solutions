# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0) 
        temp = ans 
        curr = 0 
        active = False 
        while(head != None):
            if(head.val == 0):
                if(active):
                    temp.next = ListNode(curr) 
                    temp = temp.next 
                    curr = 0 
                else:
                    active = True 
            else:
                curr += head.val 
            head = head.next 

        return ans.next
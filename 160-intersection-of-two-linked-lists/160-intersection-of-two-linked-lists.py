# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        storeA = headA
        storeB = headB
        while headA != None or headB != None:
            if headA == headB:
                return headA
            elif headA == None:
                headA = storeB
            else:
                headA = headA.next
            if headB == None:
                headB = storeA
            else:
                headB = headB.next
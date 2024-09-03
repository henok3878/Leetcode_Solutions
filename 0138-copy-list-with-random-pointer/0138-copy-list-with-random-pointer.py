"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        mapping = {}
        temp = head 
        def helper(curr_org):
            if(curr_org is None):
                return 
            id1 = id(curr_org)
            curr_cpy = mapping.setdefault(id1, Node(curr_org.val))
            if(curr_org.next):
                id2 = id(curr_org.next)
                nxt_cpy = mapping.setdefault(id2, Node(curr_org.next.val))
                curr_cpy.next = nxt_cpy
            
            if (curr_org.random):
                id3 = id(curr_org.random) 
                rnd_cpy = mapping.setdefault(id3,Node(curr_org.random.val)) 
                curr_cpy.random = rnd_cpy 
            
            helper(curr_org.next)

        helper(temp)
        return mapping[id(head)]
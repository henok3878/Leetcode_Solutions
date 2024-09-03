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
        if not head: return None 
        mapping = {}
        temp = head 
        while temp:
            temp_cpy = Node(temp.val) 
            mapping[id(temp)] = temp_cpy 
            temp = temp.next 

        temp = head 
        temp_cpy = mapping[id(temp)]
        while temp_cpy:
            if temp.random:
                temp_cpy.random = mapping[id(temp.random)] 
            if temp.next:
                temp_cpy.next = mapping[id(temp.next)]
            temp = temp.next 
            temp_cpy = temp_cpy.next 
        
        return mapping[id(head)]
            
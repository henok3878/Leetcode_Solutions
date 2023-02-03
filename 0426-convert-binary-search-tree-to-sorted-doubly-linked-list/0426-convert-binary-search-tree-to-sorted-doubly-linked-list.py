"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        dummy_head = tail = Node() 
        
        def inorder(node):
            nonlocal dummy_head, tail 
            if not node:
                return
            inorder(node.left) 
            tail.right = node 
            node.left = tail 
            tail = node 
            inorder(node.right) 
        if not root:
            return None 
        inorder(root) 
        head = dummy_head.right 
        head.left = tail 
        tail.right = head 
        return head 
                
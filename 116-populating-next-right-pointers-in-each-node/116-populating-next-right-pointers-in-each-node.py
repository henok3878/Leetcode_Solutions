"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root or root.left is None and root.right is None:
            return root
        root.left.next = root.right
        root.right.next = root.next.left if root.next else None
        l_t = self.connect(root.left)
        r_t = self.connect(root.right)
        return root 
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
    def connect(self, root: 'Node') -> 'Node':
        if (not root):
            return root
        
        q = deque()
        q.append(root)
        
        while(len(q) > 0):
            size = len(q)
            curr = []
            for i in range(size):
                p = q.popleft()
                curr.append(p)
                if p.left != None:
                    q.append(p.left)
                if p.right != None:
                    q.append(p.right)
            for i in range(size - 1):
                curr[i].next = curr[i + 1]
        
        return root
            
            
        
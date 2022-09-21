# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root,0)]
        #0: st, 1: left, 2: process, 3: right 
        
        ans = []
        while stack: 
            node, nxt = stack.pop()
            if nxt == 0:
                if not node:
                    continue 
                stack.append((node,2))
                stack.append((node.left,0)) 
            elif nxt == 2:
                ans.append(node.val)
                stack.append((node.right, 0)) 
        
        return ans 
            
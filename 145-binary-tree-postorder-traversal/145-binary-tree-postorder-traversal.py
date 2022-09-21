# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root,0)] 
        #0: st, 1: left, 2: right, 3:process
        ans = []
        while stack: 
            node, nxt = stack.pop() 
            if nxt == 0:
                if not node:
                    continue 
                stack.append((node,1))
            elif nxt == 1:
                stack.append((node,2))
                stack.append((node.left,0))
            elif nxt == 2:
                stack.append((node,3)) 
                stack.append((node.right, 0)) 
            elif nxt == 3:
                ans.append(node.val)
        return ans 
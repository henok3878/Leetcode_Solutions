# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            l.append(node.val) 
            inorder(node.right)
            
        l = []
        inorder(root)
        for i in range(1, len(l)):
            if l[i] <= l[i-1]:
                return False 
        return True 

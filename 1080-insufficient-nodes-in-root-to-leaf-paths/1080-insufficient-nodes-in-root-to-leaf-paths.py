# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        if not root:
            return None
        elif root.left == root.right: 
            return None if limit > root.val else root 
        root.left = self.sufficientSubset(root.left, limit - root.val) 
        root.right = self.sufficientSubset(root.right,limit - root.val) 
        
        return root if root.left != root.right else None 
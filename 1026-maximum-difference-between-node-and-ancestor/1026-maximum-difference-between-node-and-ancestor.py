# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        self.mx = 0 
        def helper(node,mn,mx):
            if node is None:
                return 
            mx = max(mx, node.val) 
            mn = min(mn, node.val) 
            self.mx = max(mx - mn, self.mx)
            helper(node.left,mn, mx) 
            helper(node.right,mn, mx) 
        
        helper(root,root.val, root.val) 
        
        return self.mx 
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
            self.mx = max(abs(mn-node.val),abs(mx - node.val), self.mx) 
            helper(node.left,min(mn, node.val), max(mx, node.val)) 
            helper(node.right, min(mn, node.val), max(mx, node.val)) 
        
        helper(root,root.val, root.val) 
        
        return self.mx 
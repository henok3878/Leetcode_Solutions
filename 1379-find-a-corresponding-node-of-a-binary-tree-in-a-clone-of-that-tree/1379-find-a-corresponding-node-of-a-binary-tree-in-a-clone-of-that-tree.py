# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        
        def helper(root, tgt):
            if root.val == tgt:
                return root
            res = None
            if(root.left):
                res = helper(root.left,tgt)
            if(not res and root.right):
                res = helper(root.right,tgt)
            
            return res
        return helper(cloned,target.val)
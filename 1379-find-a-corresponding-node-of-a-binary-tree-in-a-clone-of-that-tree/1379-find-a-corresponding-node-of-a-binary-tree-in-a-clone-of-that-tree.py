# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        # Follow up
        def dfs(root1, root2):
            if(not root1):
                return
            if(root1 == target):
                return root2
            
            left = dfs(root1.left,root2.left)
            if(left):
                return left
            return dfs(root1.right,root2.right)
        
                
        return dfs(original,cloned)
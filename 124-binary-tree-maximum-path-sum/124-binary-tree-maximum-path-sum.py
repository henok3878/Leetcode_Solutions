# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_path_sum = float('-inf')
        
        def helper(node):
            
            if not node:
                return 0 
            nonlocal max_path_sum 
            left = helper(node.left) 
            right = helper(node.right) 
            
            max_path_sum = max(left + right + node.val, max_path_sum) 
            single_path = max(node.val, max(left, right) + node.val)
            max_path_sum = max(single_path, max_path_sum) 
            
            return single_path 
            
        
        helper(root)
        
        return max_path_sum 
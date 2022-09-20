# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from sortedcontainers import SortedList 
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        offset_l = 0
        offset_r = 0  
        grid = defaultdict(lambda: SortedList())
        def helper(node,row,col):
            nonlocal offset_l 
            nonlocal offset_r
            
            if not node:
                return 
            offset_l = min(offset_l, col) 
            offset_r = max(offset_r,col)
            grid[col].add((row,node.val))
            helper(node.left, row + 1, col - 1) 
            helper(node.right, row + 1, col + 1)
            
        helper(root,0,0) 
        ans = []
        for col in range(offset_l, offset_r + 1):
            ans.append([v for r,v in grid[col]]) 
        return ans 
            
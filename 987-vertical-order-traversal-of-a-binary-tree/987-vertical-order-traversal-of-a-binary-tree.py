# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from sortedcontainers import SortedList 
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        offset = [0,0]
        grid = defaultdict(lambda: SortedList())
        def helper(node,row,col):
            if not node:
                return 

            offset[0], offset[1] = min(offset[0],col), max(offset[1],col)
            grid[col].add((row,node.val))
            
            helper(node.left, row + 1, col - 1) 
            helper(node.right, row + 1, col + 1)
            
        helper(root,0,0) 
        ans = []
        for col in range(offset[0], offset[1] + 1):
            ans.append([v for r,v in grid[col]]) 
        return ans 
            
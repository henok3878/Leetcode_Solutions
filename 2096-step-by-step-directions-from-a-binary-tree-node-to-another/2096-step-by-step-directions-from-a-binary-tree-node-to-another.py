# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        

        
        def find_node(val, node, path):
            if not node:
                return None
            if node.val == val:
                return path
            path.append("R")
            right = find_node(val, node.right, path)
            if right:
                return right 
            path.pop()
            path.append("L")
            left = find_node(val, node.left, path)
            if left:
                return left
            path.pop()
            
        path1 = find_node(startValue,root,[])
        path2 = find_node(destValue,root,[])
        
        ans = []
        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] == path2[i]:
                i += 1 
            else:
                break
        for idx in range(i,len(path1)):
            ans.append('U')
        for idx in range(i, len(path2)):
            ans.append(path2[idx])
            
        return "".join(ans)
        
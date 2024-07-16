# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        lowestParent = root 
        def getLowestParent(val1, val2, node):
            nonlocal lowestParent 
            val = 0
            if node is None:
                return 0
            elif node.val == val1 or node.val == val2:
                val = 1 + getLowestParent(val1, val2, node.left) + getLowestParent(val1, val2, node.right) 
            else:
                val = getLowestParent(val1, val2, node.left) + getLowestParent(val1, val2, node.right) 
            if val == 2:
                lowestParent = node 
                val = 0 
            return val 

        def getPath(val, node, curr, reverse):
            if node is None:
                return []
            elif node.val == val:
                return curr[:]
            else:
                curr.append( ("U" if reverse else "L"))
                left = getPath(val, node.left, curr, reverse )
                curr.pop()
                if(left):
                    return left 

                curr.append( ("U" if reverse else "R"))
                right = getPath(val, node.right, curr, reverse) 
                curr.pop()
                return right 
        
        getLowestParent(startValue, destValue, root) 
        path1 = getPath(startValue,lowestParent, [], True)
        path2 = getPath(destValue,lowestParent, [], False)
        return "".join(path1 + path2)
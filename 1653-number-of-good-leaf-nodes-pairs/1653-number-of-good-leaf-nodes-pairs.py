# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:

        ans = 0
        
        def is_leaf(node):
            return node and node.left is None and node.right is None 
            
        def traverse(node):
            if not node:
                return defaultdict(int)

            curr = defaultdict(int) 
            if is_leaf(node):
                curr[0] = 1 
            else:
                left = traverse(node.left) 
                right = traverse(node.right) 
                for l in left.keys():
                    curr[l + 1] = left[l]
                    for r in right.keys():
                        if l + r + 2 <= distance:
                            nonlocal ans
                            ans += left[l] * right[r] 
                for k in right.keys():
                    curr[k + 1] += right[k]
            # print(node.val, curr)
            return curr 

        traverse(root)
        return ans 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        total = 0
        queue = deque()
        queue.append(root)
        
        while(len(queue) > 0):
            size = len(queue)
            total = 0
            for i in range(size):
                curr = queue.popleft()
                total += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return total
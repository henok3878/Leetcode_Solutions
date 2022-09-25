# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(node):
            if not node:
                return 'x' 
            return '('+str(node.val)+')' + preorder(node.left) + preorder(node.right) 
        s = preorder(root)
        # print(s)
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(itr):
            val = next(itr) 
            num = ''
            if val == 'x':
                return None 
            elif val == '(':
                while 1:
                    val = next(itr)
                    if val == ')':
                        break 
                    num += val 
            # print(num)
            # print("val", val)
            return TreeNode(int(num),helper(itr), helper(itr))
        return helper(iter(data))
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
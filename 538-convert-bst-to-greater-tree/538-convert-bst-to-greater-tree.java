/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode convertBST(TreeNode root) {
        
        helper(root,0);
        
        return root;
    }
    
    private int helper(TreeNode node, int greater){
        if(node == null)
            return greater;
        int right = helper(node.right,greater);
        node.val += right;
        int left = helper(node.left,node.val);
        return left;
    }
}
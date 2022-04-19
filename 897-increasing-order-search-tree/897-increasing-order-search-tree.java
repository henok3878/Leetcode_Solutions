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
    TreeNode temp;
    public TreeNode increasingBST(TreeNode root) {
        temp = new TreeNode();
        TreeNode ans = temp;
        helper(root);
        return ans.right;
    }
    
    private void helper(TreeNode root){
        if(root == null) return;
        helper(root.left);
        root.left = null;
        temp.right = root;
        temp = temp.right;
        helper(root.right);
    }
}
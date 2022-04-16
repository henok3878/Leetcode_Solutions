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
        node.val += helper(node.right,greater);
        
        return helper(node.left,node.val);
    }
}
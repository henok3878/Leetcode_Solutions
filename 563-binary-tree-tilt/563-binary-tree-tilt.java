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
    public int findTilt(TreeNode root) {
        int[] ans = findTiltHelper(root);
        return ans[0];
    }
    
    private int[] findTiltHelper(TreeNode root){
        if(root == null) return new int[]{0,0};
        
        int[] left = findTiltHelper(root.left);
        int[] right = findTiltHelper(root.right);
        
        return new int[]{left[0] + right[0] + Math.abs(left[1] - right[1]), root.val + left[1] + right[1]}; 
    }
}
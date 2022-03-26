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
    int sum = 0;
    public int sumNumbers(TreeNode root) {
        if(root == null) return 0;
        dfs(root,0);
        return sum;
    }
    
    private void dfs(TreeNode node, int path){
        if(node.left == null && node.right == null)
            sum += (path * 10) + node.val;
        else{
            if(node.left != null) dfs(node.left,(path * 10) + node.val);
            if(node.right != null) dfs(node.right, (path * 10) + node.val);
        }
    }
}
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
        dfs(root,"");
        return sum;
    }
    
    private void dfs(TreeNode node, String path){
        if(node.left == null && node.right == null)
            sum += Integer.parseInt(path + node.val);
        else{
            if(node.left != null) dfs(node.left,path + node.val);
            if(node.right != null) dfs(node.right, path + node.val);
        }
    }
}
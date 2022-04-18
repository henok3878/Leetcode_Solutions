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
    int number = -1;
    int cnt  = 0;
    public int kthSmallest(TreeNode root, int k) {
        dfs(root,k);
        return number;
    }
    private void dfs(TreeNode root,int k){
        if(root.left != null)
            dfs(root.left,k);
        cnt++;
        if(k == cnt){
            number = root.val;
            return;
        }
        if(root.right != null)
            dfs(root.right,k);
    }
}
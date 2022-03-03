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
    TreeNode prev = null;
    TreeNode first = null;
    TreeNode last = null;
    
    public void recoverTree(TreeNode root) {
        inOrder(root);
        int temp = first.val;
        first.val = last.val;
        last.val = temp;
    }
    
    private void inOrder(TreeNode node){
        if(node == null) return;
        inOrder(node.left);
        if(prev != null && prev.val >= node.val){
            first = (first == null) ? prev : first;
            last = node;
        }
        prev = node;
        inOrder(node.right);
    }
}
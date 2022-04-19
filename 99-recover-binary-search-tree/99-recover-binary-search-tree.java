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
    
    TreeNode prevprev;
    TreeNode prev;
    TreeNode temp;
    public void recoverTree(TreeNode root) {
                
        recover(root);

        int temp = prevprev.val;
        prevprev.val = prev.val;
        prev.val = temp;
        
    }
    
    public void recover(TreeNode curr){
        if(curr == null) return;
        recover(curr.left);
        if(temp != null && temp.val > curr.val){
            if(prevprev == null){
                prevprev = temp;
            }
            prev = curr;
        }
        temp = curr;
        recover(curr.right);
    }
}
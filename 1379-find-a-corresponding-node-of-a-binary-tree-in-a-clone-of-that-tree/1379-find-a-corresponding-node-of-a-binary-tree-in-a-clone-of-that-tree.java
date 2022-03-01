/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public final TreeNode getTargetCopy(final TreeNode original, final TreeNode cloned, final TreeNode target) {
        return dfs(original,cloned,target);
    }
    
    private TreeNode dfs(TreeNode orginal, TreeNode copy, TreeNode target){
        if(orginal == null || copy == null) return null;
        if(target == orginal && orginal.val == copy.val) return copy;
        
        TreeNode left = dfs(orginal.left,copy.left, target);
        TreeNode right = dfs(orginal.right, copy.right, target);
        
        return (left == null) ? right : left; 
        
    }
}
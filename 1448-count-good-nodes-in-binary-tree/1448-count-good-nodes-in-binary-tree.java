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

    public int goodNodes(TreeNode root) {
        return dfs(root,Integer.MIN_VALUE);
    }
    
    private int dfs(TreeNode root,int maxSofar){
        if(root == null) return 0;
        return ((root.val >= maxSofar) ? 1 : 0 ) + dfs(root.left,Math.max(root.val, maxSofar)) + dfs(root.right,Math.max(root.val, maxSofar));
    }
}

/*
st: 5:05 

test: 5:12 
sub: 5:13
*/
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
    
    int count = 0;

    public int goodNodes(TreeNode root) {
        dfs(root,Integer.MIN_VALUE);
        return count;
    }
    
    private void dfs(TreeNode root,int maxSofar){
        if(root == null) return;
        count += (root.val >= maxSofar) ? 1 : 0;
        maxSofar = Math.max(root.val, maxSofar);
        dfs(root.left,maxSofar);
        dfs(root.right,maxSofar);
    }
}

/*
st: 5:05 

test: 5:12 

*/
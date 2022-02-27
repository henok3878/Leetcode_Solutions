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
    int max = 0;
    public int widthOfBinaryTree(TreeNode root) {
        Map<Integer,Integer> leftMost = new HashMap<>();
        dfs(root,leftMost,0,1);
        return max;
    }
    
    private void dfs(TreeNode root,Map<Integer,Integer> left, int level, int pos){
        if(root == null) return;
        left.putIfAbsent(level,pos);
        max = Math.max(pos - left.get(level) + 1, max);
        dfs(root.left, left,level + 1, pos*2 + 1);
        dfs(root.right, left, level + 1, pos*2 + 2);
        
    }
}


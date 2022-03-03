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
    public TreeNode lcaDeepestLeaves(TreeNode root) {
        return dfs(root,1).lca;
    }
    
    private State dfs(TreeNode node, int depth){
        if(node == null) return new State(null,0);
        
        State left = dfs(node.left, depth + 1);
        left.depth += 1;
        State right = dfs(node.right, depth + 1);
        right.depth += 1;
        
        return (left.depth == right.depth) ? new State(node,left.depth) : (left.depth > right.depth) ? left : right;
    }
    
    
}

class State{
    int depth;
    TreeNode lca;
    
    public State(TreeNode lca, int depth){
        this.lca = lca;
        this.depth = depth;
    }
}
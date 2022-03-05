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
    public List<Integer> rightSideView(TreeNode root) {
        
        List<Integer> ans = new ArrayList<>();
        if(root == null) return ans;
        
        dfs(root,ans,0);
        return ans;
    }
    
    private void dfs(TreeNode root, List<Integer> ans, int h){
        if(root == null) return;
        if(ans.size() == h) ans.add(root.val);
        dfs(root.right, ans,h + 1);
        dfs(root.left, ans, h+1);
    }
}

/*
st: 2:25 
sub: 2:32 

*/
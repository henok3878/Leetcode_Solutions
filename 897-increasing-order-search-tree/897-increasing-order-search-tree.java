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
    public TreeNode increasingBST(TreeNode root) {
        List<Integer> vals = new ArrayList<>();
        helper(root,vals);
        TreeNode ans = new TreeNode();
        TreeNode temp = ans;
        for(int val : vals){
            temp.right = new TreeNode(val);
            temp = temp.right;
        }        
        return ans.right;
    }
    
    private void helper(TreeNode root, List<Integer> vals){
        if(root == null) return;
        helper(root.left,vals);
        vals.add(root.val);
        helper(root.right,vals);
    }
}
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
    public List<TreeNode> generateTrees(int n) {
        return helper(1,n);
    }
    
    private List<TreeNode> helper(int st, int end){
        List<TreeNode> list = new ArrayList<>();
        if(st > end){
            list.add(null);
            return list;
        }
        
        for(int i = st; i <= end; i++){
            
            List<TreeNode> left = helper(st,i-1);
            List<TreeNode> right = helper(i+1,end);
            for(TreeNode l : left){
                for(TreeNode r : right){
                    TreeNode nd = new TreeNode(i,l,r);
                    list.add(nd);
                }
            }
        }
        return list;
    }
}
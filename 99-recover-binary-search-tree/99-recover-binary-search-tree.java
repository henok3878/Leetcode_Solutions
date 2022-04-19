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
    List<TreeNode> list = new ArrayList<>();
    public void recoverTree(TreeNode root) {
        recover(root);
        int prevprev = -1, prev = -1;
        for(int i = 1; i < list.size(); i++){
            if(list.get(i).val < list.get(i - 1).val){
                if(prev == -1)
                    prevprev = i-1;
            
                prev = i;
            }
        }
        if(prev != -1){
            int pp = list.get(prevprev).val;
            int p = list.get(prev).val;
            list.get(prevprev).val = p;
            list.get(prev).val = pp;
        }
        
    }
    
    public void recover(TreeNode root){
        if(root == null) return;
        recover(root.left);
        list.add(root);
        recover(root.right);
    }
}
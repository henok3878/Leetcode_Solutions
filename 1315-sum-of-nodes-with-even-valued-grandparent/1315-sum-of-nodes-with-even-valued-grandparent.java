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
    public int sumEvenGrandparent(TreeNode root) {
        return sumEvensHelper(root,false,false);
    }
    
    private int sumEvensHelper(TreeNode node, boolean gp, boolean p){
        if(node == null) return 0;
        
        int left = sumEvensHelper(node.left,p,node.val%2 == 0);
        int right = sumEvensHelper(node.right,p, node.val%2 == 0);
        
        return (gp == true) ?  left + right + node.val : left + right;
    }
}

/*
st: 3:19


*/
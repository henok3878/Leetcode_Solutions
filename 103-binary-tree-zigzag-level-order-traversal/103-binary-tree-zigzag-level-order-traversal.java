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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<>();
        if(root == null) return ans;

        queue.add(root);
        boolean isLR = true;
        while(!queue.isEmpty()){
            int size = queue.size();
            List<Integer> currLevel = new LinkedList<>();
            
            for(int i = 0; i < size; i++){
                TreeNode curr = queue.poll();
                if(isLR) currLevel.add(curr.val);
                else currLevel.add(0,curr.val);
                
                if(curr.left != null) queue.add(curr.left);
                if(curr.right != null) queue.add(curr.right);
            }
            isLR = !isLR;
            ans.add(currLevel);
        }
        
        return ans;
        
    }
}

/*
st: 9:03 

sub: 9:18 

*/
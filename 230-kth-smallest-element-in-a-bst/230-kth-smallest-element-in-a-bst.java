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
    public int kthSmallest(TreeNode root, int k) {
        Queue<Integer> pq = new PriorityQueue<Integer>((a,b) -> b - a);
        dfs(root,k,pq);
        return pq.peek();
    }
    
    private void dfs(TreeNode node, int k, Queue<Integer> pq){
        if(node == null) return;
        pq.add(node.val);
        if(pq.size() > k ) pq.poll(); 
        dfs(node.left, k, pq);
        dfs(node.right,k,pq);
    }
}
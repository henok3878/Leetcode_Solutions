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
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        Map<String,Integer> count = new HashMap<>();
        List<TreeNode> ans = new ArrayList<>();
        dfs(root,count,ans);
        return ans;
    }
    
    private String dfs(TreeNode node,Map<String,Integer> count, List<TreeNode> ans){
        if(node == null) return "X";
        String left = dfs(node.left,count,ans);
        String right = dfs(node.right,count,ans);
        String curr =  node.val +" "+left+ " "+right;
        int cnt = count.getOrDefault(curr,0) + 1;
        if(cnt == 2) ans.add(node);
        count.put(curr,cnt);
        return curr;
    }
}

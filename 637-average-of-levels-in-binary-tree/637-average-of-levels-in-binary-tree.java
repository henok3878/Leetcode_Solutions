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
    public List<Double> averageOfLevels(TreeNode root) {
        
        Queue<TreeNode> queue = new LinkedList<>(); // 
        List<Double> ans = new ArrayList<>();
        queue.add(root);
        
        while(!queue.isEmpty()){
            int size = queue.size();
            List<Integer> currLevel = new ArrayList<>();
            for(int i = 0; i < size; i++){
                TreeNode curr = queue.poll();
                currLevel.add(curr.val);
                if(curr.left != null) queue.add(curr.left);
                if(curr.right != null) queue.add(curr.right);
            }
            ans.add(findAvg(currLevel));
        }
        
        return ans;
        
    }
    
    private double findAvg(List<Integer> nums){
        // finds avg for a given list of numbers  
        /*
        [9,20] => avg = 9 + 10, size = 2;
        */
        double avg = 0; 
        int size = nums.size();
        for(int num : nums) avg += num; 
        
        return avg/size;
    }
}

/*
   
   queue = [3]
   queue = [20,9]
        queue = [9,15,7] // , 20
        queue = [15,7], 9
    

*/
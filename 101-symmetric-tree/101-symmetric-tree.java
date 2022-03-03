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
    public boolean isSymmetric(TreeNode root) {
       
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        
        while(!queue.isEmpty()){
            int size = queue.size();
            List<Integer> currLevel = new ArrayList<>();
            
            for(int i = 0 ; i < size; i++){
                TreeNode curr = queue.poll();
                currLevel.add(curr.left == null ? -101 : curr.left.val);
                if(curr.left != null) queue.add(curr.left);
                currLevel.add(curr.right == null ? -101 : curr.right.val);
                if(curr.right != null) queue.add(curr.right);
                                                                                                }
            if(!isSymmetric(currLevel)) return false;
        }
        
        return true;
    }
    
    private boolean isSymmetric(List<Integer> list){
        int st = 0, size = list.size();
        while(st < size / 2){
            if(list.get(st) != list.get(size - 1 - st)) return false;
            st++;
        }
        return true;
    }
    
}

/*
    Trick: Check the level below you not the level you are in
        ex:       2   level 1
                 / \  level 2
                 \ /\ level 3 
                 by default level 1 is always valid becuase it contains a single element 
                 stand at level 1 and check if level 2 is valid if it is valid 
                 stand at level 2 and check if level 3 is valid and keep doing 

*/
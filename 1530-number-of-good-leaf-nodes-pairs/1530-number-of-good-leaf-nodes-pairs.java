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
    
    Map<TreeNode,List<TreeNode>> graph = new HashMap<>();
    Set<TreeNode> leafs = new HashSet<>();
    
    public int countPairs(TreeNode root, int distance) {
        
        build(root,null);
        //for(TreeNode l : leafs) System.out.println(l.val);
        int count = 0;
        for(TreeNode leaf : leafs){
            
            Queue<TreeNode> queue = new LinkedList<>();
            Set<TreeNode> visited = new HashSet<>();
            queue.add(leaf);
            visited.add(leaf);
            int level = 0;  
            while(!queue.isEmpty() && level <= distance){
                int size = queue.size();
                for(int i = 0; i < size; i++){
                    TreeNode curr = queue.poll();
                    if(level > 0 && leafs.contains(curr)){
                        count++;
                        continue;
                    }
                    for(TreeNode adj : graph.get(curr)){
                        if(!visited.contains(adj)){
                            queue.add(adj);
                            visited.add(adj);
                        }
                    }
                }
                level++;
                
            }
              
        }
            
        return count/2;
    }
    
    private void build(TreeNode root,TreeNode parent){
        if(root == null) return;
        
        build(root.left,root);
        build(root.right,root);
        graph.putIfAbsent(root,new ArrayList<>());
        if(parent != null){
            graph.putIfAbsent(parent,new ArrayList<>());
            graph.get(parent).add(root);
            graph.get(root).add(parent);
        }
        if(root.left == null && root.right == null)
            leafs.add(root);
    }    
}


/*
st: 4:37 
    
    Let assume I have a helper function : bool isLeaf(N)


*/
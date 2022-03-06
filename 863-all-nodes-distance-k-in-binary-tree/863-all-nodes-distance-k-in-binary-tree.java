/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        buildGraph(root, graph);
        List<Integer> ans = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();
        visited.add(target.val);
        queue.add(target.val);
        int dist = 0;
        while(!queue.isEmpty()){
            if(dist == k){
                ans.addAll(queue);
                break;
            }
            int size = queue.size();
            for(int i = 0; i < size; i++){
                int curr = queue.poll();
                for(int adj : graph.get(curr)){
                    if(!visited.contains(adj)){
                        queue.add(adj);
                        visited.add(adj);
                    }
                }
                
            }
            dist++;
                    


        }
        
        return ans;
    }
    
    private void buildGraph(TreeNode root, Map<Integer,List<Integer>> graph){
        if(root == null) return;
        List<Integer> rootAdjs = graph.getOrDefault(root.val,new ArrayList<>());
        if(root.left != null){
             List<Integer> leftAdjs = graph.getOrDefault(root.left.val, new ArrayList<>());         rootAdjs.add(root.left.val);
             leftAdjs.add(root.val);
            graph.put(root.left.val, leftAdjs);
        }
        if(root.right != null){
            List<Integer> rightAdjs = graph.getOrDefault(root.right.val, new ArrayList<>());        rightAdjs.add(root.val);
            rootAdjs.add(root.right.val);
            graph.put(root.right.val,rightAdjs);
        }
        graph.put(root.val,rootAdjs);
        buildGraph(root.left,graph);
        buildGraph(root.right,graph);
        
    }
}
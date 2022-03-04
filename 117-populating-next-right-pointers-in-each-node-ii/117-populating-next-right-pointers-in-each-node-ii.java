/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        if(root == null) return null;
        Queue<Node> queue = new LinkedList<>();
        queue.add(root);
        
        while(!queue.isEmpty()){
            List<Node> currLevel = new ArrayList<>();
            int size = queue.size();
            for(int i = 0; i < size; i++){
                Node curr = queue.poll();
                currLevel.add(curr);
                if(curr.left != null) queue.add(curr.left);
                if(curr.right != null) queue.add(curr.right);
            }
            connecter(currLevel);
        }
        
        return root;
    }
    
    private void connecter(List<Node> nodes){
        int size = nodes.size();
        for(int i = 0; i < size - 1; i++) nodes.get(i).next = nodes.get(i + 1);
        nodes.get(size - 1).next = null;
    }
}

/*
    Solution 1: Using BFS O(N) extra space 
        st: 10:08 
        test: 10:18 
        sub : 10:19 
        
    Solution 2: 
        st: 10:23 
        test: 10:40
            -> got stuck 


*/
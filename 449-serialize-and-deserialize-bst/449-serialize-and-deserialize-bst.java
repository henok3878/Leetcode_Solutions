/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if(root == null) return "";
        StringBuilder sb = new StringBuilder();
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        
        while(!queue.isEmpty()){
            TreeNode curr = queue.poll();
            sb.append(curr.val + " ");
            if(curr.left != null) queue.add(curr.left);
            if(curr.right != null) queue.add(curr.right);
        }
        return sb.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if(data.isEmpty()) return null;
        
        List<String> tree = Arrays.asList(data.split(" "));
        TreeNode root = new TreeNode(Integer.parseInt(tree.get(0)));         for(int i = 1; i < tree.size(); i++){
            TreeNode temp = root;
            addNode(temp,Integer.parseInt(tree.get(i)));
        }   
        return root;
    }
    
    private void addNode(TreeNode root, int val){
        if(val > root.val){
            if(root.right == null)
                root.right = new TreeNode(val);
            else addNode(root.right,val);
        }
        else {
            if(root.left == null) root.left = new TreeNode(val);
            else addNode(root.left,val);
        }
        
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// String tree = ser.serialize(root);
// TreeNode ans = deser.deserialize(tree);
// return ans;
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
class BSTIterator {
    
    List<TreeNode> list;
    int idx;
    
    public BSTIterator(TreeNode root) {
        list = new ArrayList<>();    
        idx = -1;
        init(root);
    }
    
    public int next() {
        return list.get(++idx).val;
    }
    
    public boolean hasNext() {
        if(idx <  list.size() - 1)
            return true;
        return false;
            
    }
    private void init(TreeNode root){
        if(root == null) return;
        init(root.left);
        list.add(root);
        init(root.right);
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */
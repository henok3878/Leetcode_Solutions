class Solution {
    
    TrieNode root;
    
    public List<Integer> lexicalOrder(int n) {
        root = new TrieNode();
        
        /*
            whole for loop: O(n*len(n)) 
                -> len(n) <= 5, becuase 1 <= n <= 5*10^4 
                O(n*5) = 
                O(n)
            
        */
        for(int num = 1; num <= n; num++)
            insert(num); // O(len(n))
        
        List<Integer> ans = new ArrayList<>();
        
        /*
            O(n)
        */
        traverseTrie(ans,root);
        return ans;
        
    }
    
    private void traverseTrie(List<Integer> ans, TrieNode node){
        if(node == null) return;
        else if(node.isEnd) ans.add(node.data);
        for(int i = 0; i < 10; i++){
            if(node.children[i] != null){
                traverseTrie(ans,node.children[i]);
            }
        }
    }
    
    private void insert(int num){
        String numStr = num + "";
        TrieNode temp = root;
        for(int i = 0; i < numStr.length(); i++){
            int charIdx = numStr.charAt(i) -'0';
            if(temp.children[charIdx] == null)
                temp.children[charIdx] = new TrieNode();
            temp = temp.children[charIdx];
        }
        temp.isEnd = true;
        temp.data = num;
    }
}

class TrieNode{
    boolean isEnd;
    TrieNode[] children;
    int data;
    public TrieNode(){
        children = new TrieNode[10];
    }
    
}

/*
    

*/
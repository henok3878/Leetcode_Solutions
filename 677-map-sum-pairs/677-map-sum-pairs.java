class MapSum {

    TrieNode root;
    
    public MapSum() {
        root = new TrieNode();
    }
    
    public void insert(String key, int val) {
        TrieNode temp = root;
        for(int i = 0;i < key.length(); i++){
            int charIdx = key.charAt(i) - 'a';
            if(temp.children[charIdx] == null){
                temp.children[charIdx] = new TrieNode();
            }
            temp = temp.children[charIdx];
        }
        temp.isEnd = true;
        temp.val = val;
    }
    
    public int sum(String prefix) {
        TrieNode temp = root;
        for(int i = 0; i < prefix.length(); i++){
            int charIdx = prefix.charAt(i) - 'a';
            if(temp.children[charIdx] == null) return 0;
            temp = temp.children[charIdx];
        }
        return dfs(temp);
    }
    
    private int dfs(TrieNode node){
        if(node == null) return 0;
        int sum = node.isEnd ? node.val : 0 ;
            
        for(TrieNode child : node.children){
            sum += dfs(child);
        }
        
        return sum;
        
    }
}

class TrieNode{
    boolean isEnd;
    TrieNode[] children;
    int val;
    
    public TrieNode(){
        isEnd = false;
        children = new TrieNode[26];
    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.insert(key,val);
 * int param_2 = obj.sum(prefix);
 */
class Trie {
    
    Node root;
    public Trie() {
        root = new Node();
    }
    
    public void insert(String word) {
        Node temp = root;
        for(int i = 0; i < word.length(); i++){
            int c = word.charAt(i) - 'a';
            if(temp.children[c] == null)  
                temp.children[c] = new Node();
            
            temp = temp.children[c];
        }
        temp.isWord = true;
    }
    
    public boolean search(String word) {
        Node temp = root;
        for(int i = 0; i < word.length(); i++){
            int c = word.charAt(i) - 'a'; 
            if(temp.children[c] == null) return false;
            temp = temp.children[c];
        }
        return temp.isWord;
    }
    
    public boolean startsWith(String prefix) {
        Node temp = root;
        
        for(int i = 0; i < prefix.length(); i++){
            int c = prefix.charAt(i) - 'a';
            if(temp.children[c] == null) return false;
            temp = temp.children[c];
        }
        return true;
    }
}
class Node{
    boolean isWord;
    Node[] children;
    
    public Node(){
        children = new Node[26];
    }
    
}
/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
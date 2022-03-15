class Solution {
    
    TrieNode root;
    
    public String replaceWords(List<String> dictionary, String sentence) {
        root = new TrieNode();
        buildTrie(dictionary);
        String[] words = sentence.split(" ");
        
        for(int i = 0; i < words.length; i++)
            words[i] = findRoot(words[i]);
        
        return String.join(" ", words);
    }
    
    private String findRoot(String word){
        TrieNode temp = root;
        StringBuilder sb = new StringBuilder();
        
        for(int i = 0; i < word.length(); i++){
            int currCharIdx = word.charAt(i) - 'a';
            if(temp.isWord) break;
            if(temp.children[currCharIdx] != null){
                sb.append(word.charAt(i));
                temp = temp.children[currCharIdx];
            }else break;
        }
        
        return (sb.isEmpty() || !temp.isWord) ? word : sb.toString();
    }
    
    private void buildTrie(List<String> words){
        for(String word : words) insert(word);
    }
    
    private void insert(String word){
        TrieNode temp = root;
        for(int i = 0; i < word.length(); i++){
            int currCharIdx = word.charAt(i) - 'a';
            if(temp.children[currCharIdx] == null){
                temp.children[currCharIdx] = new TrieNode();
            }
            temp = temp.children[currCharIdx];
        }
        temp.isWord = true;
    }
    
}

class TrieNode{
    
    boolean isWord;
    TrieNode[] children;
    
    public TrieNode(){
        children = new TrieNode[26]; // lowercase alphabates 
    }
}
class Solution {
    
    TrieNode root;
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        root = new TrieNode();
        
        for(String word : products) insert(word);
        
        List<List<String>> ans = new ArrayList<>();
        
        TrieNode temp = root;
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < searchWord.length(); i++){
            List<String> curr = new ArrayList<>();
            int currCharIdx = searchWord.charAt(i) - 'a'; // currChar - 'a'
            if(temp.children[currCharIdx] != null){
                sb.append(searchWord.charAt(i) + "");
                temp = temp.children[currCharIdx];
                recommend(temp,curr,sb); 
                ans.add(curr);
            }else break;
        }
        
        while(ans.size() != searchWord.length()) ans.add(new ArrayList<>());
        
        return ans;
        
    }
    
    
    private void recommend(TrieNode node, List<String> ans, StringBuilder soFar){
        if(node == null || ans.size() == 3) return;
        else if(node.isWord) ans.add(soFar.toString());
        
        for(int i = 0; i < 26; i++){
            if(node.children[i] != null){
                soFar.append((char)(i + 'a') + "");
                recommend(node.children[i],ans, soFar);   
                soFar.deleteCharAt(soFar.length() - 1);
            }
           
        }
    }
    
    private void insert(String word){
        TrieNode temp = root;
        for(int i = 0; i < word.length(); i++){
            int c = word.charAt(i) - 'a';
            if(temp.children[c] == null){
                temp.children[c] = new TrieNode();
            }
            temp = temp.children[c];
        }
        temp.isWord = true;
    }
}

class TrieNode{
    boolean isWord;
    TrieNode[] children;
    
    public TrieNode(){
        this.children = new TrieNode[26];
    }
}
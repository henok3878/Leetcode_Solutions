class Solution {
    
    TrieNode root;
    Map<String,Boolean> dp;
    public boolean wordBreak(String s, List<String> wordDict) {
        root = new TrieNode();
        dp = new HashMap<>();
        
        for(String word : wordDict) insert(word);
        
        return dfs(s);
        
    }
    
    private boolean dfs(String word){
        int n = word.length();
        if(n == 0 || searchWord(word)) return true;
        
        if(dp.containsKey(word)) return dp.get(word);
        
        for(int i = 0; i < n; i++){
            String first = word.substring(0,i);
            String second = word.substring(i);
            if(searchWord(first)){
                if(dfs(second)){
                    dp.put(second,true);
                    return true;
                }
            }
        }
        dp.put(word, false);
        return false;
    }
    

    
    private boolean searchWord(String word){
        //System.out.println("search: " + word);
        TrieNode temp = root;
        for(int i = 0; i < word.length(); i++){
            int currIdx = word.charAt(i) - 'a';
            if(temp.children[currIdx] == null) return false;
            temp = temp.children[currIdx];
        }
        
        return temp.isWord;
    }
    
    private void insert(String word){
        TrieNode temp = root;
        for(int i = 0; i < word.length(); i++){
            int currIdx = word.charAt(i) - 'a';
            if(temp.children[currIdx] == null){
                temp.children[currIdx] = new TrieNode();
            }
            temp = temp.children[currIdx];
        }
        temp.isWord = true;
    }
    
}

class TrieNode{
    boolean isWord;
    TrieNode[] children;
    
    public TrieNode(){
        children = new TrieNode[26];
    }
    
}

/*

catsanddog:

cat, sand, dog
cats, and, dog

        

*/
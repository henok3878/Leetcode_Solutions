class Solution {
    String ans = "";
    TrieNode root;
    public String longestWord(String[] words) {
        root = new TrieNode();
        Arrays.sort(words);

        for(String word : words){
            boolean isValid = insert(word);

            if(isValid && ans.length() < word.length()){
                ans = word;
            }
        }
        
        return ans;
    }
    
    private boolean insert(String word){
        TrieNode temp = root;
        boolean isValid = true;
        int wordLen = word.length();
        for(int i = 0; i < wordLen; i++){
            int charIdx = word.charAt(i) - 'a';
            if(temp.children[charIdx] == null){
                isValid = (i < wordLen - 1) ? false : isValid;
                if(!isValid) break;
                temp.children[charIdx] = new TrieNode();
            }
            temp = temp.children[charIdx];
            if(i < wordLen - 1 && !temp.isEnd){
                isValid = false;
                break;
            }
        }
        temp.isEnd = true;
        return isValid;
        
    }
}
class TrieNode{
    boolean isEnd;
    TrieNode[] children;
    
    public TrieNode(){
        children = new TrieNode[26];
    }
    
}
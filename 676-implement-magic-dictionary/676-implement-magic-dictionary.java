class MagicDictionary {
    
    Set<String> words;
    public MagicDictionary() {
        words = new HashSet<>();
    }
    
    public void buildDict(String[] dictionary) {
        for(String dict : dictionary) words.add(dict);
    }
    
    public boolean search(String searchWord) {
        
        for(int i = 0; i < searchWord.length(); i++){
            StringBuilder sb = new StringBuilder(searchWord);
            for(int c = 0; c < 26; c++){
                char ch = (char)(c + 'a');
                if(ch == searchWord.charAt(i)) continue;
                sb.setCharAt(i,ch);
                if(words.contains(sb.toString())) return true;
            }
        }
        return false;
    }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary obj = new MagicDictionary();
 * obj.buildDict(dictionary);
 * boolean param_2 = obj.search(searchWord);
 */
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList ){
        
        Set<String> words = new HashSet<>();
        for(String word : wordList) words.add(word);
        
        Set<String> visited = new HashSet<>();
        Queue<String> queue = new LinkedList<String>();
        queue.add(beginWord);
        visited.add(beginWord);
        int level = 1;
        while(!queue.isEmpty()){
            int size = queue.size();
            for(int l = 0; l < size; l++){
                String curr = queue.poll();
                if(curr.equals(endWord)) return level;
                for(String adj : findAdj(curr,words)){
                    if(!visited.contains(adj)){queue.add(adj); visited.add(adj);}
                }
            }
            
            level++;
        }
        
        return 0;
    }
                            
    private List<String> findAdj(String word, Set<String> words){
        List<String> res = new ArrayList<>();
        for(int i = 0; i < word.length(); i++){
            StringBuilder sb = new StringBuilder(word);
            for(int ch = 0; ch < 26 ; ch++){
                char c = (char)(ch + 'a');
                sb.setCharAt(i,c);
                String rep = sb.toString();
                if(words.contains(rep)) res.add(rep);
            }            
        }
        
        return res;
    }
}

/*
st: 4:36 


beginWord = "hit", endWord = "cog", 

wordList = ["hot","dot","dog","lot","log","cog"]

hit -> [*it, h*t,hi*] => [hot,]

    hot -> [*ot,h*t,*ot] => [dot,lot]
        
        dot -> [*ot, d*t,do*] => [dog], hot and dot are alredy processed 
            
            dog -> [*og,d*g,do*] -> [cog,log] 
            
        lot -> [*ot, l*t,lo*] => Terminate (Return)

*/
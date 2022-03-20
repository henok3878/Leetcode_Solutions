class Solution {
    public String smallestStringWithSwaps(String s, List<List<Integer>> pairs) {
        
        int n = s.length();
        if(n < 2 || pairs.size() == 0) return s;
        
        UnionFind uf = new UnionFind(n);
        
        Map<Integer,List<Integer>> rootToIndices = new HashMap<>();
        
        for(List<Integer> pair : pairs){
            uf.union(pair.get(0), pair.get(1));
        }
        
        for(int idx = 0; idx < n ; idx++){
            int root = uf.find(idx);
            List<Integer> indices = rootToIndices.getOrDefault(root,new ArrayList<>());
            indices.add(idx);
            rootToIndices.put(root,indices);
            
        }
        
        char[] smallestCharArray = new char[n];
                
        for(int key : rootToIndices.keySet()){
            List<Character> chars = new ArrayList<>();
            List<Integer> indices = rootToIndices.get(key);
            
            for(int idx : indices) chars.add(s.charAt(idx));

            Collections.sort(chars);
            
            for(int j = 0; j < chars.size(); j++){
                smallestCharArray[indices.get(j)] = chars.get(j);
            }
             
        }
        
        return new String(smallestCharArray);
         
    }
}

class UnionFind{
    
    int[] parents;
    int[] ranks;
    
    public UnionFind(int size){
        parents = new int[size];
        ranks = new int[size];
        for(int i = 0; i < size; i++) parents[i] = i;
    }
    
    public int find(int elem){
        if(parents[elem] == elem) return elem;
        return parents[elem] = find(parents[elem]);
    }
    
    public void union(int elem1, int elem2){
        int parent1 = find(elem1);
        int parent2 = find(elem2);
        
        if(parent1 == parent2) return; // there is  a cycle 
        
        if(ranks[parent1] > ranks[parent2])
            parents[parent2] = parent1;
        else if(ranks[parent1] < ranks[parent2])
            parents[parent1] = parent2;
        else{
            parents[parent2] = parent1;
            ranks[parent1]++;
        }
    }
}
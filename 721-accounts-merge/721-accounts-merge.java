class Solution {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        int n = accounts.size();
        UnionFind uf = new UnionFind(n);
        Map<String,Integer> emailToIdx = new HashMap<>();
        
        for(int i = 0; i < n; i++){
            List<String> acc = accounts.get(i);
            for(int j = 1; j < acc.size(); j++){
                String email = acc.get(j);
                if(emailToIdx.containsKey(email)){
                    uf.union(i,emailToIdx.get(email));
                }else{
                    emailToIdx.put(email,i);
                }       
            }
        }
        
        Map<Integer,List<String>> components = new HashMap<>();
        
        for(String email : emailToIdx.keySet()){
            int idx = emailToIdx.get(email);
            int parent = uf.find(idx);
            List<String> curr = components.getOrDefault(parent,new ArrayList<>());
            curr.add(email);
            components.put(parent,curr);
        }
        
        List<List<String>> ans = new ArrayList<>();
        
        for(int idx : components.keySet()){
            List<String> curr = components.get(idx);
            Collections.sort(curr);
            String name = accounts.get(idx).get(0);
            curr.add(0,name);
            ans.add(curr);
        }
        
        return ans;
        
    }
}
class UnionFind{
    int[] parents;
    int[] ranks;
    
    public UnionFind(int size){
        parents = new int[size];
        ranks = new int[size];
        
        for(int i = 0; i < size; i++){
            parents[i] = i;
        }
    }
    
    public int find(int elem){
        if(parents[elem] == elem) return elem;
        
        return parents[elem] = find(parents[elem]); // path compression 
    }
    
    public void union(int elem1, int elem2){
        int parent1 = find(elem1);
        int parent2 = find(elem2);
        
        if(parent1 == parent2) return;

        if(ranks[parent1] > ranks[parent2]){
            parents[parent2] = parent1;
        }
        else if(ranks[parent1] < ranks[parent2]){
            parents[parent1] = parent2;
        }
        else{
            parents[parent2] = parent1;
            ranks[parent2]++;
        }
    }
    
}
/*

["John","johnsmith@mail.com","john_newyork@mail.com"],

["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],

["John","johnnybravo@mail.com"]



*/
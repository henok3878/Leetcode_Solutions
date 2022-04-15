class Solution {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        int n = accounts.size();
        
        UnionFind uf = new UnionFind(n);
        
        Map<String,Integer> emailToIdx = new HashMap<>();
        for(int i = 0;i < n; i++){
            List<String> acc = accounts.get(i);
            for(int j = 1;j < acc.size(); j++){
                String email = acc.get(j);
                if(emailToIdx.containsKey(email))
                    uf.union(emailToIdx.get(email),i);
                else 
                    emailToIdx.put(email,i);
            }            
        }
        Map<Integer,List<String>> emails = new HashMap<>();
        for(String email : emailToIdx.keySet()){
            int p = uf.find(emailToIdx.get(email));
            List<String> ems = emails.getOrDefault(p,new ArrayList<>());
            ems.add(email);
            emails.put(p,ems);
        }
        
        List<List<String>> ans =new LinkedList<>();
        for(int rep : emails.keySet()){
            String name = accounts.get(rep).get(0);
            List<String> ems = emails.get(rep);
            Collections.sort(ems);
            ems.add(0,name);
            ans.add(ems);
        
        }
        
        return ans;
    }
}

class UnionFind{
    int[] parents;
    int[] ranks;
    
    public UnionFind(int n){
        parents = new int[n];
        for(int i = 0; i < n; i++)
            parents[i] = i;
        ranks = new int[n];
    }
    
    public int find(int el){
        if(parents[el] == el) 
            return el;
        return parents[el] = find(parents[el]);
    }
    
    public void union(int el1, int el2){
        int p1 = find(el1);
        int p2 = find(el2);
        if(p1 == p2)
            return;
        if(ranks[p1] > ranks[p2])
            parents[p2] = p1;
        else if(ranks[p1] < ranks[p2])
            parents[p1] = p2;
        else {
            parents[p2] = p1;
            ranks[p1]++;
        }
    }
}
class Solution {
    public int longestConsecutive(int[] nums) {
        
        int n = nums.length;
        if(n == 0) return 0;
        
        UnionFind uf = new UnionFind(n);
        
        Map<Integer,Integer> numToIdx = new HashMap<>();
        
        for(int i = 0; i < n; i++){
            if(numToIdx.containsKey(nums[i])) continue;
            if(numToIdx.containsKey(nums[i] - 1)){
                uf.union(i,numToIdx.get(nums[i]-1));
            }
            if(numToIdx.containsKey(nums[i] + 1)){
                uf.union(i,numToIdx.get(nums[i] + 1));
            }
            numToIdx.put(nums[i],i);
        }
        
        return uf.largestSize();
        
    }
}

class UnionFind{
    
    int[] parents;
    int[] sizes;
    
    public UnionFind(int size){
        parents = new int[size];
        sizes = new int[size];
        for(int i = 0; i < size; i++){
            parents[i] = i;
            sizes[i] = 1;
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
        
        if(sizes[parent1] >= sizes[parent2]){
            sizes[parent1] += sizes[parent2];
            parents[parent2] = parent1;
        }
        else{
            sizes[parent2] += sizes[parent1];
            parents[parent1] = parent2;
        }
    }
    
    public int largestSize(){
        int largest = Integer.MIN_VALUE;
        for(int num : sizes) largest = Math.max(largest, num);
        
        return largest;
    }
}


/*
100 

4 , 3 

200 

1 ,2 


*/
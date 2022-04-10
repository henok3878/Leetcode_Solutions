class Solution {
    public List<String> findAllRecipes(String[] recipes, List<List<String>> ingredients, String[] supplies) {
        
        Map<String,Integer> idx = new HashMap<>();
        Set<String> sups = new HashSet<>();
        Set<String> recps = new HashSet<>();
    
        for(int i =0; i < recipes.length; i++){
            idx.put(recipes[i],i);
            recps.add(recipes[i]);
        }
        for(int i = 0; i < supplies.length; i++){
            sups.add(supplies[i]);
        }
        
        List<String> ans = new ArrayList<>();
        for(String rec : recipes){
            if(isPos(rec,sups,recps,ingredients,idx, new HashSet<String>())){
                ans.add(rec);
                sups.add(rec);
            }
        }
        
        return ans;
    }
    
    private boolean isPos(String rec, Set<String> sup, Set<String> recipes, List<List<String>> ing, Map<String,Integer> idx, Set<String> v){
        if(!sup.contains(rec) && !recipes.contains(rec))
            return false;
        if(sup.contains(rec))
            return true;
        else if(v.contains(rec))
            return false;
        v.add(rec);
        
        for(String in : ing.get(idx.get(rec))){
            if(!isPos(in,sup,recipes,ing,idx,v))
                return false;
        }
        v.remove(rec);
        return true;
    }
}

/*
Input:
recipes = ["bread"], 
ingredients = [["yeast","flour"]], 
supplies = ["yeast","flour","corn"]
Output: ["bread"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".



*/
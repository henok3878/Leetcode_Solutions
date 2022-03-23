class Solution {
    public List<String> findAllRecipes(String[] recipes, List<List<String>> ingredients, String[] supplies) {
        
        Set<String> pos = new HashSet<>(Arrays.asList(supplies));
        Set<String> impos = new HashSet<>();
        Map<String,Set<String>> graph = new HashMap<>();
        for(int i = 0; i < recipes.length; i++)
            graph.put(recipes[i],new HashSet<>(ingredients.get(i)));
        
        List<String> ans = new ArrayList<>();
        for(int i = 0; i < recipes.length; i++){
            String recipe = recipes[i];
            if(pos.contains(recipe)) ans.add(recipe);
            else if(!impos.contains(recipe)){
                    if(isPossible(recipe,pos,impos,graph)){
                        ans.add(recipe);
                        pos.add(recipe);
                    }
                    else impos.add(recipe);
            }
        }
        
        return ans;
    }
    
    private boolean isPossible(String recipe, Set<String> pos, Set<String> impos, Map<String,Set<String>> graph){
        if(pos.contains(recipe)) return true;
        else if(!graph.containsKey(recipe) || impos.contains(recipe)) return false;
        impos.add(recipe);
        for(String adj : graph.get(recipe)){
            if(graph.getOrDefault(adj,new HashSet<>()).contains(recipe)){
                // cycle 
                impos.add(adj);
                impos.add(recipe);
                return false;
            }
            else if(!isPossible(adj,pos,impos,graph)){
                impos.add(adj);
                impos.add(recipe);
                return false;
            }
        }
        impos.remove(recipe);
        pos.add(recipe);
        return true;
    }
}

/*
is not possible if, 1) there is a dependency cycle 

                        Happens if my ingredients contains me.
                        
                    2) ingredient is not found in ingredients list 
                    
           ["p","we","bxgnm","vpio","i","hjvu","igi","anp","tokfq","z","kwdmb","g","qb","q",hthy"]
           
[
---
---
["fzr","wi","otr","xgp","wbjr","igi","b"],["fzr","xgp","wi","otr","tokfq","izcad","igi","xevvq","i","anp"],["wi","xgp","wbjr"],["wbjr","bxgnm","i","b","hjvu","izcad","igi","z","g"],["xgp","otr","wbjr"],["wbjr","otr"],["wbjr","otr","fzr","wi","xgp","hjvu","tokfq","z","kwdmb"],["xgp","wi","wbjr","bxgnm","izcad","p","xevvq"],["bxgnm"],["wi","fzr","otr","wbjr"], ---
["wbjr","wi","fzr","xgp","otr","g","b","p"],
["otr","fzr","xgp","wbjr"],---
["xgp","wbjr","q","vpio","tokfq","we"],
["wbjr","wi","xgp","we"], 
["wbjr"],---
["wi"]], ---

["wi","otr","wbjr","fzr","xgp","xevvq","g","izcad","b"]  

o:p = [0]
*/


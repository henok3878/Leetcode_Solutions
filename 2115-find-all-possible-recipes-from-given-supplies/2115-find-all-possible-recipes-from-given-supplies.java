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
            else if(!impos.contains(recipe) && isPossible(recipe,pos,impos,graph))                    ans.add(recipe);
        }
        
        return ans;
    }
    
    private boolean isPossible(String recipe, Set<String> pos, Set<String> impos, Map<String,Set<String>> graph){
        if(pos.contains(recipe)) return true;
        else if(!graph.containsKey(recipe) || impos.contains(recipe)) return false;
        impos.add(recipe);
        for(String adj : graph.get(recipe)){
           if(!isPossible(adj,pos,impos,graph)){
                impos.add(adj);
                return false;
            }
        }
        impos.remove(recipe);
        pos.add(recipe);
        return true;
    }
}



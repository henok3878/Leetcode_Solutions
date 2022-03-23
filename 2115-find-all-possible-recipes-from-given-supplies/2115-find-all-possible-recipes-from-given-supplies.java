class Solution {
    public List<String> findAllRecipes(String[] recipes, List<List<String>> ingredients, String[] supplies) {
     
        Set<String> supp = new HashSet<String>(Arrays.asList(supplies));
        Map<String,Boolean> isPossible = new HashMap<>();
        List<String> ans = new ArrayList<>();
        Map<String,List<String>> graph = new HashMap<>();
        for(int i = 0; i < recipes.length; i++){
            graph.put(recipes[i],ingredients.get(i));
        }
        for(int i = 0; i < recipes.length; i++){
                if(isRecipePossible(recipes[i],isPossible,graph,supp))
                    ans.add(recipes[i]);
        }
        
        return ans;
    }
    
    private boolean isRecipePossible(String recipe, Map<String,Boolean> isPossible,Map<String,List<String>> ingredients, Set<String> supplies){
        if(supplies.contains(recipe)) return true;
        else if(isPossible.containsKey(recipe)) return isPossible.get(recipe);
        else if(!ingredients.containsKey(recipe)) return false;

        isPossible.put(recipe,false);
        for(String ing : ingredients.get(recipe)){
            if(!isRecipePossible(ing,isPossible,ingredients,supplies)){
                return false;
            }
        }
        
        isPossible.put(recipe,true);
        return true;
    }
}
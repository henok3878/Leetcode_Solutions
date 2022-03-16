class Solution {
    public List<Integer> lexicalOrder(int n) {
        List<Integer> ans = new ArrayList<>();
        
        for(int i = 1; i < 10; i++)
            dfs(i,n,ans);
        
        return ans;
        
    }
    
    private void dfs(int curr, int n, List<Integer> ans){
        if(curr > n) return;
        
        ans.add(curr);
        for(int i = 0; i < 10; i++){
            dfs(10*curr + i,n,ans);
        }
    }
    
}
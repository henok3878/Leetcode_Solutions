class Solution {
    public List<Integer> goodDaysToRobBank(int[] security, int time) {
        int n = security.length;
        int[] before = new int[n];
        int[] after = new int[n];
        
        for(int i = 1; i < n; i++){
            if(security[i] <= security[i-1])
                before[i] = before[i-1] + 1;
        }
        for(int i = n-2; i >= 0; i--){
            if(security[i] <= security[i+1])
                after[i] = after[i+1] + 1;
        }
        List<Integer> ans = new ArrayList<>();
        
        for(int i = 0;i < n; i++){
            if(before[i] >= time && after[i] >= time)
                ans.add(i);
        }
        
        return ans;
    }
}
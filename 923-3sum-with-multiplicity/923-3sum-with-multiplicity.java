class Solution {
    int MOD = (int)Math.pow(10,9) + 7;
    public int threeSumMulti(int[] arr, int target) {
        int n = arr.length;
        
        
        
        int ans = 0;
        for(int i = 0; i < n; i++){
            int[] counts = new int[301];
            for(int j = i + 1; j < n; j++){
                //System.out.println(Arrays.toString(counts));
                int comp = target - (arr[i] + arr[j]);
                if(comp >= 0 && counts[comp] > 0){
                    ans += counts[comp];
                    ans %= MOD;
                }
                counts[arr[j]]++;
            }
        }
        
        return ans;
    }
}
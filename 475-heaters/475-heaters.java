class Solution {
    public int findRadius(int[] houses, int[] heaters) {
        Arrays.sort(houses);
        Arrays.sort(heaters);
        int htrs = heaters.length;
        int ans = Integer.MIN_VALUE;
        
        int prev = 0;
        for(int i = 0; i < houses.length; i++){
            int near = find(prev,houses[i],heaters);
            prev = near;
            //System.out.println("h: " + houses[i]  + " , near: " + near);
            int curr = -1;
            if(near < 0){
                curr = heaters[0] - houses[i];
            }else if(near >= htrs){
                curr = houses[i] - heaters[htrs-1];
            }
            else{
                int left = (near - 1 >= 0) ? Math.abs(houses[i] - heaters[near-1]) : Integer.MAX_VALUE;
                int right = Math.abs(houses[i] - heaters[near]);
                curr = Math.min(left,right);
            }
            ans = Math.max(curr,ans);
        }
        return ans;
        
    }
    
    private int find(int i, int val, int[] hs){
        int st = i, end = hs.length-1;
        while(st <= end){
            int mid = st + (end - st) /2 ;
            if(hs[mid] < val){
                st = mid + 1;
            }
            else end = mid - 1;
        }
        return st;
    }
}
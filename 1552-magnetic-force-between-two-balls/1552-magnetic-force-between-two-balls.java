class Solution {
    public int maxDistance(int[] position, int m) {
        int n = position.length;
        Arrays.sort(position);
    
        int st = 1;
        int end = position[n-1];
        
        int best = 0;
        
        while(st <= end){
            int mid = st + (end - st) / 2;
            if(isValid(position,m,mid)){
                st = mid + 1;
                best = mid;
            }else{
                end = mid - 1;
            }
        }
        return best;
    }
    
    
    private boolean isValid(int[] pos, int m, int force){
        
        int last = -1*force;
        for(int i = 0; i < pos.length; i++){
            if(pos[i] - last >= force){
                m--;
                last = pos[i];
            }
        }
        
        return m<= 0;
    }
}
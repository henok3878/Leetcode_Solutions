class Solution {
    public int minCost(String colors, int[] neededTime) {
        int time = 0;
        
        
        for(int i = 1; i < colors.length(); i++){
            if(colors.charAt(i) == colors.charAt(i - 1)){
                if(neededTime[i - 1] > neededTime[i]){
                    time += neededTime[i];
                    swap(neededTime,i-1,i);

                }else time += neededTime[i-1];
            }
        }
        return time;
    }
    
    private void swap(int[] time, int i , int j){
        int temp = time[i];
        time[i] = time[j];
        time[j] = temp;
    }
}

/*
colors = "aabaa", neededTime = [1,2,3,4,1]


*/
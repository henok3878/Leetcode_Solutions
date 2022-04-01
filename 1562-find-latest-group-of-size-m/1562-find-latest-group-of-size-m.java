class Solution {
    public int findLatestStep(int[] arr, int m) {
        int n = arr.length;
        int[] len = new int[n+2];
        
        int count = 0;
        int latest = -1;
        for(int i = 0;i < n; i++){
            int curr = arr[i], left = len[arr[i] - 1], right = len[arr[i] + 1];
            if(left == m) count--;
            if(right == m) count--;
            len[curr] = len[curr-left] = len[curr + right] =  left + right + 1;
            
            if(len[curr] == m) count++;
            
            if(count > 0) latest = i + 1;
            
        }
        
        return latest;
    }
}

/*


--84248328

-$***$--^**^--


*/
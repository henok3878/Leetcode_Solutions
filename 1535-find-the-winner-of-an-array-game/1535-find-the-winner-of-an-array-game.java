class Solution {
    public int getWinner(int[] arr, int k) {
        int n = arr.length;
        
        int left = 0;
        int right;
        int max = -1;
        while(left < n){
            right  = left;
            while(right < n && arr[left] >= arr[right]){
                max = Math.max(arr[right],max);
                right++;
            }
            int count = (left == 0) ? right - left - 1  : right - left;
            if(count >= k)
                return arr[left];
            left = right;
        }
        
        return max;
        
    }
}

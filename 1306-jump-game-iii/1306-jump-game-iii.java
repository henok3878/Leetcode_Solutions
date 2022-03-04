class Solution {
    public boolean canReach(int[] arr, int start) {
        if(start < 0 || start >= arr.length || arr[start] < 0) return false;
        else if(arr[start] == 0) return true;
        int left = start - arr[start], right = start + arr[start];
        arr[start] *= -1;
        return canReach(arr,left) || canReach(arr,right);
    }
}

/*
    st: 2 : 28
    
    end: 2:43 

*/
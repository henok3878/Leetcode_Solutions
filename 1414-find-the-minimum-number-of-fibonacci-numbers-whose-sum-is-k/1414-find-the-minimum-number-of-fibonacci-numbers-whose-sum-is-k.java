class Solution {
    public int findMinFibonacciNumbers(int k) {
        int prev = 1, curr = 1;
        while(curr + prev <= k){
            curr += prev;
            prev = curr - prev;
        }
        int count = 0;

        while(k > 0){
            if(k - curr >= 0){
                k -= curr; 
                count++;
            }
            prev = curr - prev;
            curr -= prev;
        }
        
        return count;
    }
}
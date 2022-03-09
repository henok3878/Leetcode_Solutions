class Solution {
    public boolean divisorGame(int n) {
        return helper(n,true);
    }
    private boolean helper(int n, boolean turn){
        if(n == 2) return turn;
        else if(n < 2) return !turn;
        
        for(int x = 1; x < n; x++){
            if(n % x == 0){
                if(helper(n - x,!turn) == turn) return turn;
                else return !turn;
            }
        }
        
        return !turn;
    }
}
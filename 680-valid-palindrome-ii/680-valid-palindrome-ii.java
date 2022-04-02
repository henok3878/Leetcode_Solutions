class Solution {
    public boolean validPalindrome(String s) {
        for(int i =0, j = s.length() - 1; j >= 0 && i < s.length(); i++, j--){
            if(s.charAt(i) != s.charAt(j)){
                return isPal(s,i+1,j) || isPal(s,i,j-1);
            }
        }
        
        return true;
    }
    
    private boolean isPal(String s, int i, int j){
        if(i >= j) return true;
        else if(s.charAt(i) != s.charAt(j)) return false;
        
        return isPal(s,i+1,j-1);
    }
}


/*
    abacba
      ""
      
    "a b a"
       ""
    "abca"
      ||

*/
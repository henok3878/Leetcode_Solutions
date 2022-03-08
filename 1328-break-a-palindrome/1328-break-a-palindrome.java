class Solution {
    public String breakPalindrome(String palindrome) {
        
        int n = palindrome.length();
        
        StringBuilder sb = new StringBuilder(palindrome);
        if(n == 1) return "";
        for(int i = 0; i < n; i++){
            int curr = sb.charAt(i) - 'a';
            if((n %2 == 0 || i != n/2) && curr != 0){
                sb.setCharAt(i,(char)(0 + 'a'));
                return sb.toString();
            }
        }
        if(sb.toString().equals(palindrome)){
            sb.setCharAt(n-1,'b');
        }
        return sb.toString();
    }
}


/*

st: 3:20
sub: 3:36
  "abccba"
   ------ 
   
   make first smallest possible if it is already the smallest 
   make the next smallest possible and keep going 


*/
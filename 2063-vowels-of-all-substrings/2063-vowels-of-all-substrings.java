class Solution {
    public long countVowels(String word) {
        int n = word.length();
        long ans = 0;
        for(int i = 0; i < n;i++){
            if(isVowel(word.charAt(i)))
             ans +=  (long)(n-i) * (i + 1);
             //ans += (n - i) * (i + 1); 
        }
        return ans;
    }
    
    private boolean isVowel(char c){
        if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
            return true;
        return false;
    }
}

/*
s = "-----i-j---------"
total pairs = N*N = N^2

bruteforce = N*(N^2)

 N + N 


*/
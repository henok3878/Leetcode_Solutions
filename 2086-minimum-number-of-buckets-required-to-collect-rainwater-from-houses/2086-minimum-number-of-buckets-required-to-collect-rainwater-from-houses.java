class Solution {
    public int minimumBuckets(String street) {
        int n = street.length();
        char[] s = street.toCharArray();
       
        int count = 0;
        
        for(int i = 0; i < n; i++){
           if(s[i] == 'H'){
               char prev = (i-1 >= 0) ? s[i-1] : ' ';
               char nxt = (i + 1 < n) ? s[i+1] : ' ';
               if(prev == 'B') continue;
               else if(nxt == '.'){
                   s[i+1] = 'B';
                   count++;
               }
               else if(prev == '.'){
                   s[i-1] = 'B';
                   count++;
               }
               else{
                   return -1;
               }
           }
        }
        
        return count;
    }  
}

/*
if poss choose '.' that is in the middle 

 .H.H.. 
 
 H.H.H
 
 d = #dots
 
 max valid str = d * 2;
 
 
 
 


*/
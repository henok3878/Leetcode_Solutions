class Solution {
    public int minAddToMakeValid(String s) {
        int opening = 0, moves = 0;
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '(') opening++;
            else{
                if(opening == 0) moves++;
                else opening--;
            }            
        }
        return moves + opening;
    }
}

/*
st: 3:03 
sub: 3:19 
cases: 
    - ""
    - "()"
    - "()()"
    


*/
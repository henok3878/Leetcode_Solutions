class Solution {
    public int minFlips(String target) {
        int n = target.length();
        char[] init = new char[n];
        Arrays.fill(init,'0');
        
        int flips = 0;
        boolean isFliped = false;
        for(int i = 0; i < n; i++){
            if(isFliped){
                if(target.charAt(i) == init[i]){
                    flips++;
                    isFliped = false;
                }
            }else if(target.charAt(i) != init[i]){
                isFliped = true;
                flips++;
            }
        }
        return flips;
    }
}

/*
st: 3:45 

sub: 4:09

target: 10111
init  : 00000   
        00111
        11000
        10111

*/
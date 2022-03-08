class Solution {
    public String predictPartyVictory(String senate) {
        char[] senates = senate.toCharArray();
        int n = senates.length;
        int radiant = 0, dire = 0;
        
        for(int i = 0; i < n;i++) {
            if(senates[i] == 'R') radiant++;
            else dire++;
        }
        int start = 0;
        while(radiant > 0 && dire > 0){
            if(senates[start] != 'R' && senates[start] != 'D'){
                start = (start + 1) % n;
            }
            else{
                char currBanned = 'R'; 
                if(senates[start] == 'R'){
                    currBanned = 'D';
                    dire--;
                }else radiant--;
                int nxt = (start + 1) % n;
                start = nxt;
                while(senates[nxt] != currBanned){
                    nxt = (nxt + 1) % n;
                }
                senates[nxt] = ' ';
            }
        }
        
        return (radiant > 0) ? "Radiant" : "Dire";
    }
}

/*
st: 3:37 
sub: 4:16 
*/
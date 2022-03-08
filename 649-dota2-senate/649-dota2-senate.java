class Solution {
    public String predictPartyVictory(String senate) {
        char[] senates = senate.toCharArray();
        int n = senate.length();
        int radiant = 0, dire = 0, start = 0;
        
        for(int i = 0; i < n;i++) {
            if(senates[i] == 'R') radiant++;
            else dire++;
        }
        
        while(radiant > 0 && dire > 0){
            while (senates[start] != 'R' && senates[start] != 'D') {
                start = (start + 1) % senates.length;
            }
            
            char ban = 'R';
            if (senates[start] == 'R') {
                ban = 'D';
                dire--;
            }
            else radiant--;
            
            int idx = (start + 1) % senates.length;
            while (senates[idx] != ban) {
                idx = (idx + 1) % senates.length;
            }
            
            senates[idx] = ' ';
            start = (start + 1) % senates.length;
        }
        
        return (radiant > 0) ? "Radiant" : "Dire";
    }
}

/*
st: 3:37 

        
        while (r > 0 && d > 0) {
       
        }
        
        return d == 0 ? "Radiant" : "Dire";

"RDR"
 |

*/
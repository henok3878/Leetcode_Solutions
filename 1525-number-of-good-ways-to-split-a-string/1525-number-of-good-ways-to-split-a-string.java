class Solution {
    public int numSplits(String s) {
        int n = s.length();
        int[] s1 = new int[26];
        int[] s2 = new int[26];
        int s1count = 1, s2count = 0;
        s1[s.charAt(0) - 'a']++;
        for(int i = 1; i < n; i++) {
            if(s2[s.charAt(i) - 'a'] == 0) s2count++;
            s2[s.charAt(i) - 'a']++;
        }
        int ans = (s1count == s2count) ? 1 : 0;
        
        for(int i = 1; i < n; i++){
            int curr = s.charAt(i) - 'a';
            if(s1[curr] == 0) s1count++;
            s1[curr]++;
            s2[curr]--;
            if(s2[curr] == 0) s2count--;
            ans+= (s1count == s2count) ? 1 : 0;
        }
        
        return ans;
        
    }
}

/*
    s ---split---> (sLeft, sRight)
        
        if(sLeft + sRight == s && #distnict(sLeft) == #distnict(sRight)) 
            meaning the split is good.




"a | acaba" , s1Count = 1, s2Count = 3
"aa | caba" , s1Count = 1, 
"aac | aba"
"aaca | ba"
"aacab | a"


*/
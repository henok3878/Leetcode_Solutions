class Solution {
    public List<Integer> partitionLabels(String s) {
        int[] lastIdx = new int[26];
        for(int i = 0; i < s.length() ; i++) lastIdx[s.charAt(i) - 'a'] = i;
        
        List<Integer> ans = new ArrayList<>();
        
        int max = -1;
        int st = 0;
        for(int i = 0; i < s.length(); i++){
            max = Math.max(lastIdx[s.charAt(i) - 'a'], max);
            if(max == i){
                ans.add(max - st + 1);
                st = i + 1;
                max = -1;
            }
        }
        return ans;
    }
}
/*
st: 1:35 
sub: 1:52
"ababcbacadefegdehijhklij"
 

[a: 8, b:5 ]

*/
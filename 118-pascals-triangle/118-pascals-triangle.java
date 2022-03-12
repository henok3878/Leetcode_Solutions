class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ans = new ArrayList<>();
        ans.add(Arrays.asList(1));
        for(int i = 2; i <= numRows; i++){
            List<Integer> curr = new ArrayList<>();
            for(int j = 0;j < i; j++){
                int left = (j - 1 < 0) ? 0 : ans.get(i-2).get(j-1);
                int right = (j < (i -1 )) ? ans.get(i-2).get(j) : 0;
                curr.add(left + right);
            }
            ans.add(curr);
        }
        return ans;
    }
}
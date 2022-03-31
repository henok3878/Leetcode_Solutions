class Solution {
    public List<Integer> mostVisited(int n, int[] rounds) {

        List<Integer> ans = new ArrayList<>();
        int st = rounds[0], end = rounds[rounds.length - 1];
        if(st <= end){
            for(int i = st; i <= end;i++)   ans.add(i);
        }else{
            for(int i = 1; i <= end; i++) ans.add(i);
            for(int i = st; i <= n; i++) ans.add(i);
        }

        return ans;
    }
}
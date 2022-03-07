class Solution {
    public int[][] reconstructQueue(int[][] people) {
        int m = people.length, n = people[0].length;
        
        Arrays.sort(people,(a,b) -> (b[0] == a[0]) ? a[1] - b[1] : b[0] - a[0]);
        List<List<Integer>> temp = new ArrayList<>();
        
        for(int[] person : people){
            int idx = person[1];
            temp.add(idx,Arrays.asList(person[0],person[1]));
        }
        
        int[][] ans = new int[m][n];
        int idx = 0;
        for(List<Integer> item : temp)
            ans[idx++] = new int[]{item.get(0),item.get(1)};
        
        return ans;   
    }
}
class Solution {
    public List<List<Integer>> shiftGrid(int[][] grid, int k) {
        
        List<Integer> nums = new ArrayList<>();
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j< grid[0].length; j++){
                nums.add(grid[i][j]);
            }
        }
        
        while(k-- > 0)
            nums = shift(nums);
        
        List<List<Integer>> ans = new ArrayList<>();
        for(int i = 0; i < grid.length; i++){
            List<Integer> temp = new ArrayList<>();
            for(int j = 0;j < grid[0].length; j++){
                int idx = (i*grid[0].length) + j;
                temp.add(nums.get(idx));
            }
            ans.add(temp);
        }
        
        return ans;
    }
    
    private List<Integer> shift(List<Integer> nums){
        List<Integer> temp = new ArrayList<>();
        temp.add(nums.get(nums.size() - 1));
        for(int i = 0; i < nums.size() - 1; i++)   
            temp.add(nums.get(i));
        return temp;
    }
}

/*
1,2,3,4,5,6,7,8,9
9,1,2,
3,4,5,
6,7,8

*/
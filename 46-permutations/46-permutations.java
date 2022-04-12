class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        helper(0,nums,ans, new ArrayList<>(), new HashSet<>());
        return ans;
    }
    
    private void helper(int i, int[] nums, List<List<Integer>> ans, List<Integer> curr,Set<Integer> v){
        if(i >= nums.length){
            ans.add(new ArrayList<>(curr));
            return;
        }
        
        for(int num : nums){
            if(v.contains(num)) continue;
            curr.add(num);
            v.add(num);
            helper(i+1,nums,ans,curr,v);
            curr.remove(curr.size() - 1);
            v.remove(num);
        }
    }
}
/*
1,2,3

(n choices)     (n-1 choices)  (1 choice)
-               -  ... .....      - 


goal: choose n elements (to reach the last elem)
constraint: don't choose num that is already choosen in the current path 
state: index, choices (descion space for ith index it is n - i choices)
*/
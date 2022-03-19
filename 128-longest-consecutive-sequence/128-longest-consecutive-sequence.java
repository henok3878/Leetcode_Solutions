class Solution {
    public int longestConsecutive(int[] nums) {
        
        if(nums.length == 0) return 0;
        
        Set<Integer> visited = new HashSet<>();
        for(int num : nums) visited.add(num);
        
        int longest = Integer.MIN_VALUE;
        
        for(int num : visited){
            int current = 1;
            if(!visited.contains(num - 1)){
                 while(visited.contains(num + 1)){
                    current++;
                    num++;
                }
            }
            longest = Math.max(longest,current);
            
        }
        
        return longest;
    }
}
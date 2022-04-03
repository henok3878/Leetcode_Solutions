class Solution {
    public int numTriplets(int[] nums1, int[] nums2) {
        
        int count = 0;
        
        for(int i = 0; i < nums1.length; i++)
            count+= helper(nums2,((long)nums1[i] * nums1[i]));
            
        for(int i = 0; i < nums2.length; i++)
           count += helper(nums1,(long)Math.pow(nums2[i],2)); 
        
        return count;
    }
    
    private int helper(int[] nums,long sq){
        int count = 0;
        Map<Integer,Integer> visited = new HashMap<>();
        for(int j = 0;j < nums.length; j++){
            int curr = nums[j];
            if(sq % curr == 0.0){
                int comp = (int)(sq / curr);
                if(visited.containsKey(comp)) count += visited.get(comp);
            }
            visited.put(curr,visited.getOrDefault(curr,0) + 1);
        }
        return count;
    }
}
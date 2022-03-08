class Solution {
    public String largestNumber(int[] nums) {
        int n = nums.length;
        String[] strs = new String[n];
        for(int i = 0; i < n; i++)  strs[i] = "" + nums[i];
        
        Arrays.sort(strs,(a,b)-> (b+a).compareTo(a+b));
        
        StringBuilder sb = new StringBuilder();
        for(String s : strs) sb.append(s);
        
        while(sb.length() != 1 && sb.charAt(0) == '0' ) sb.deleteCharAt(0);
        
        return sb.toString();
    }
}
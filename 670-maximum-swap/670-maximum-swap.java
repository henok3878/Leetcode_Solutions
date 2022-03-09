class Solution {
    public int maximumSwap(int num) {
        int temp = num;
        String s = num + "";
        int size = s.length();
        int[] nums = new int[size];
        for(int i = size - 1; i >= 0; i--){
            int curr = num % 10;
            num = num/10;
            nums[i] = curr;
        }
        int[] ids = new int[10];
        Arrays.fill(ids,-1);
        for(int i = 0; i < nums.length; i++){
            ids[nums[i]] = i;
        }

        boolean isFound = false;
        for(int i = 0; i < size; i++){
            int curr = nums[i];
            
            for(int dig = 9; dig >= 1; dig--){
                if(ids[dig] == -1) continue;
                if(curr < dig){
                    nums[ids[dig]] = curr;
                    nums[i] = dig;
                    isFound = true;
                }
                else if(dig == curr && ids[curr] == i){
                    ids[curr] = -1;
                }
                break;
                
            }
            if(isFound) break;
        }
        if(!isFound) return temp;
        StringBuilder sb = new StringBuilder();
        for(int n  : nums) sb.append(n);
        return Integer.parseInt(sb.toString());
        
    }
}
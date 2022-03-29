class Solution {
    static int[] map;
    public int[] sortJumbled(int[] mapping, int[] nums) {
        map = mapping;
        Num[] temp = new Num[nums.length];
        for(int i = 0;i < nums.length; i++){
            temp[i] = new Num(nums[i],i);
        }
        Arrays.sort(temp,(a,b)->(a.changed == b.changed) ? a.idx - b.idx : a.changed - b.changed);
        
        int[] ans = new int[nums.length];
         for(int i = 0;i < nums.length; i++){
            ans[i] = temp[i].num;
        }
                
        return ans;
        
    }
}

class Num{
 
    int num;
    int idx;
    int changed;
    public Num(int num, int idx){
        this.num = num;
        this.idx = idx;
        changed = change(num);
    }
    private int change(int n){
        if(n == 0) return Solution.map[0];
        int num = 0;
        int i = 1;
        while(n > 0){
            num += i*Solution.map[n%10];
            n = n/10;
            i*=10;
        }
        return num;
    }
}


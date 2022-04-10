class Solution {
    public int calPoints(String[] ops) {
        List<Integer> ans = new ArrayList<>();
        for(int i = 0; i <  ops.length; i++){
            String str = ops[i];
            if(str.equals("+")){
                int s = ans.size();
                ans.add(ans.get(s - 1) + ans.get(s - 2));
            }
            else if(str.equals("D")){
                ans.add(ans.get(ans.size() - 1) * 2);
            }
            else if(str.equals("C")){
                ans.remove(ans.size() - 1);
            }
            else{
                ans.add(Integer.parseInt(str));
            } 
        }
        
        int sum = 0;
        for(int n : ans) sum += n;
        
        return sum;
    }
}
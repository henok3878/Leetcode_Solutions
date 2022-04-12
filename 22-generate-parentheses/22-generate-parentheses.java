class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> ans = new ArrayList<>();
        helper(n,0,0,ans,new StringBuilder());
        
        return ans;
    }
    
    private void helper(int n,int o, int c, List<String> ans, StringBuilder sb){
        if(o == n && c == n){
            ans.add(sb.toString());
            return;
        }
        if(o > c){
            sb.append(")");
            helper(n,o,c+1,ans,sb);
            sb.deleteCharAt(sb.length() - 1);

        }
        if(o < n){
            sb.append("(");
            helper(n,o+1,c,ans,sb);
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}

/*

constraint: well formed 
            if(open > close )
                you can choose )
            if(open < n)
                you can choose (
gaol: reach 2*n th index while satsfing the constraint 

state= idx 


*/
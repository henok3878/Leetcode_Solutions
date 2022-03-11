class Solution {
    public String removeKdigits(String num, int k) {
        
        Stack<Integer> stack = new Stack();
        stack.push(Character.getNumericValue(num.charAt(0)));  
        for(int i = 1; i < num.length(); i++){
            int curr = Character.getNumericValue(num.charAt(i));
            while(k != 0 && !stack.isEmpty() && stack.peek() > curr){
                stack.pop();
                k--;
            }
            stack.push(curr);
        }
        while(k-- > 0) stack.pop();
            
        
        StringBuilder sb = new StringBuilder();
        while(!stack.isEmpty())
            sb.append(stack.pop());
        
        StringBuilder ans = sb.reverse();
        while(ans.length() > 0 && ans.charAt(0)== '0') ans.deleteCharAt(0);
        
        return (ans.toString() == "") ? "0" : ans.toString();
        
    }
}
class Solution {
    public List<Boolean> camelMatch(String[] queries, String pattern) {
        
        List<Boolean> ans = new ArrayList<>();
        int pLen = pattern.length();
        for(String query : queries){
            int qPtr = 0; // specifiy idx in query 
            int pPtr = 0;
            int qLen = query.length();
            while(pPtr < pLen && qPtr < qLen){
                char queryChar = query.charAt(qPtr);
                char patternChar = pattern.charAt(pPtr);
                if(queryChar == patternChar){
                    qPtr++; 
                    pPtr++;
                }
                else if(Character.isLowerCase(queryChar)) qPtr++;
                else break;
            }
            while(qPtr < qLen && Character.isLowerCase(query.charAt(qPtr))) qPtr++;
            if(pPtr == pLen && qPtr == qLen) ans.add(true);
            else ans.add(false);
        
        }
        
        return ans;
    }
}

/*
Time Complexity: O(q*l), where: q is num of queries    
                              : l is max length of a query in queries 
                    
Space Complexity: O(q)

*/
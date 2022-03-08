class Solution {
    public int findMinFibonacciNumbers(int k) {
        List<Integer> fibList = new ArrayList<>();
        generateFib(k,fibList);
        int count = 0, i = fibList.size() - 1;
        while(i >= 0 && k > 0){
            if(k - fibList.get(i) >= 0){
                k -= fibList.get(i);
                count++;
            }
            i--;
        }
        return count;        
    }
    
    private void generateFib(int n , List<Integer> fibList){
        fibList.add(1);fibList.add(1);
        int i = 1, j = 1;
        
        while(i+j <= n){
            int temp = j;
            j = i + j;
            i = temp;
            fibList.add(j);
            
        }
    }
}
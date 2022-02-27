class Solution {
    public int minimumSum(int num) {
        int[] arr = new int[4];
        int idx = 0;
        while(num > 0) // Getting each digit
        {
            arr[idx++] = num % 10;
            num /= 10;
        }
        
        Arrays.sort(arr);
        int a = arr[0], b = arr[1], c = arr[2] , d = arr[3];
        int sum = ((a * 10) + c) + ((b*10) + d);
        
        return sum;
    }
}
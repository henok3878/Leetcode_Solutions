class Solution {
    public int integerReplacement(int n) {
        int operations = 0;
        long num = n;
        while(num > 1){
            if(num % 2 == 0) num = num/2;
            else {
                long left = num - 1, right = num + 1; left /= 2;right /= 2;
                if(left == 1 || left % 2 == 0 || right % 2 != 0) num = num - 1;
                else num = num + 1;
            }
            operations++;
        }
        return operations;
    }
}

/*

if(n is even) => n = n /2;
else n = n + 1 or n - 1;

odd + 1 = even 
odd - 1 = even 
even / 2 = even or odd 



*/
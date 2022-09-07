class Solution {
public:
    int minimumNumbers(int num, int k) {
        if(num == 0) return 0;
        vector<vector<int>> dp(num + 1, vector<int>(num + 1, 1e9)); 
        for(int i = 0;i <= num; ++i){
            dp[num][i] = 0;
        }
        int res = 1e9; 
        for(int curr = num-1; curr >= 0; curr--){
            for(int n = k; n <= num; n += 10){
                if(curr + n <= num){
                    dp[curr][n] = min(dp[curr][n], 1 + dp[curr + n][n]);
                }
                if(n - 10 >= 0){
                    dp[curr][n] = min(dp[curr][n], dp[curr][n - 10]);
                }
                if(curr == 0){
                    res = min(res, dp[curr][n]);
                }
            }
        }
        if(res >= 1e9){
            return -1;
        }else{
            return res;
        }
    }
};

/*
class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        
        if num == 0:
            return 0
        
        dp = [[float('inf')] * (num + 1) for _ in range(num + 1)] 
        for i in range(num + 1):
            dp[num][i] = 0 
            
        res = float('inf')
        for curr in range(num-1,-1,-1):
            for n in range(k,num + 1,10):
                if curr + n <= num:
                    dp[curr][n] = min(dp[curr][n],1 + dp[curr + n][n]) 
                if n - 10 >= 0:
                    dp[curr][n] = min(dp[curr][n], dp[curr][n - 10]) 
                if curr == 0:
                    res = min(res,dp[curr][n])
        return -1 if res == float('inf') else res 
    


*/
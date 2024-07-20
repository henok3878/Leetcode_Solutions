class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        R = len(rowSum) 
        C = len(colSum) 

        ans = [[0] * C for _ in range(R)] 
        for i in range(R):
            for j in range(C):
                mn = min(rowSum[i], colSum[j]) 
                rowSum[i] -= mn
                colSum[j] -= mn 
                ans[i][j] = mn
        return ans 
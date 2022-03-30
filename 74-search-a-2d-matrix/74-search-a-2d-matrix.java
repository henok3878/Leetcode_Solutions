class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        
        int rows = matrix.length; int cols = matrix[0].length;
        
        int st = 0, end = rows*cols - 1;
        while(st <= end){
            int mid = st + (end - st) / 2;
            int i = mid/cols, j = mid % cols;
            if(matrix[i][j] > target) end = mid - 1;
            else if(matrix[i][j] < target) st = mid + 1;
            else return true;
        }
        return false;
    }
}
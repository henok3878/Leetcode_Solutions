class Solution {
    int[][] adjs = {{1,0},{-1,0},{0,1},{0,-1},{1,1},{-1,-1},{-1,1},{1,-1}};
    
    public void gameOfLife(int[][] board) {
        int m = board.length;
        int n = board[0].length;
        
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                int cnt = 0, state = board[i][j];
                for(int[] adj : adjs){
                    int x = i + adj[0], y = j + adj[1];
                    if(isInBound(x,y,m,n) && board[x][y]%2 == 1){
                       cnt++;
                    }
                }
                if(state == 0 && cnt == 3){
                    board[i][j] = 2;
                }
                else if(state == 1 && cnt > 3){
                    board[i][j] = 3;
                }
                else if(state == 1 && cnt < 2){
                    board[i][j] = 3;
                }
                
            }
        }
        
        for(int i = 0; i < m;i++){
            for(int j = 0; j < n; j++){
                if(board[i][j] == 2) board[i][j] = 1;
                else if(board[i][j] == 3) board[i][j] = 0;
            }
        }
     
    }
    
    private boolean isInBound(int i, int j, int m, int n){
        if(i < 0 || j < 0 || i >= m || j >= n)
            return false;
        return true;
    }
}

class Solution {
    int[][] adjs = {{1,0},{-1,0},{0,1},{0,-1},{1,1},{-1,-1},{-1,1},{1,-1}};
    
    public void gameOfLife(int[][] board) {
        int m = board.length;
        int n = board[0].length;
        int[][] count = new int[m][n];
        
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                for(int[] adj : adjs){
                    int x = i + adj[0], y = j + adj[1];
                    if(isInBound(x,y,m,n) && board[x][y] == 1){
                        count[i][j]++;
                    }
                }   
            }
        }
        // for(int[] r : count)
        //     System.out.println(Arrays.toString(r));
        
        for(int i = 0; i < m; i++){
            for(int j = 0;j  < n; j++){
                int cnt = count[i][j];
                int state = board[i][j];
                if(state == 0 && cnt == 3){
                    board[i][j] = 1;
                }
                else if(state == 1 && cnt > 3){
                    board[i][j] = 0;
                }
                else if(state == 1 && cnt < 2){
                    board[i][j] = 0;
                }else if(state == 1 && (cnt == 3 || cnt <= 2)){
                    board[i][j] = 1;
                }
            }
        }
    }
    
    private boolean isInBound(int i, int j, int m, int n){
        if(i < 0 || j < 0 || i >= m || j >= n)
            return false;
        return true;
    }
}

/*
live -> < 2 live -> die
live -> 2 >= x <= 3 live -> live



*/
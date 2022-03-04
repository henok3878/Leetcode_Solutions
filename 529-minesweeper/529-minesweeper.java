class Solution {
    
    int[][] directions = {{0,-1},{1,0},{0,1},{-1,0},{1,1},{1,-1},{-1,1},{-1,-1}};
                          
                          
    public char[][] updateBoard(char[][] board, int[] click) {
        int clickR = click[0], clickC = click[1];
        
        Queue<int[]> queue = new LinkedList<>();
        queue.add(click);
        
        while(!queue.isEmpty()){
            int[] clk = queue.poll();
            int i = clk[0], j = clk[1];
            if(board[i][j] == 'M'){
                board[i][j] = 'X';
                return board;
            }
            else if(board[i][j] == 'E'){
                int count = adjMines(board,clk);
                if(count == 0){
                    board[i][j] = 'B';
                    for(int[] dir : directions){
                        int x = clk[0] + dir[0], y = clk[1] + dir[1];
                        if(x < 0 || y < 0 || x >= board.length || y >= board[0].length) continue;
                        if(board[x][y] == 'E' || board[x][y] == 'M') queue.add(new int[]{x,y});

                    }
                }else{
                    board[i][j] = (char)(count + '0');
                }
            }        
        }
        
        return board;
        
    }
                          
    private int adjMines(char[][] board, int[] clk){
        int count = 0;
        for(int[] dir : directions){
            int x = clk[0] + dir[0], y = clk[1] + dir[1];
            if(x < 0 || y < 0 || x >= board.length || y >= board[0].length) continue;
            count += (board[x][y] == 'M') ? 1 : 0;    
        }
        return count;
    }
}

/*
st: 3:04 
    
test: 3:33 

sub: 

*/
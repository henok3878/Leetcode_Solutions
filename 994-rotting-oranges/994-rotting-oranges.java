class Solution {
    
    public int orangesRotting(int[][] grid) {
        int[][] directions = {{0,-1},{1,0},{0,1},{-1,0}};
        int rows = grid.length, cols = grid[0].length;
        Queue<int[]> queue = new LinkedList<>();
        int total = rows * cols;
        for(int i = 0; i < rows; i++){
            for(int j = 0; j < cols;j++){
                if(grid[i][j] == 2) queue.add(new int[]{i,j});
                if(grid[i][j] == 0) total--;
            }
        }
        if(total == 0) return 0;
        
        int time = 0;
        int rotten = 0;
        while(!queue.isEmpty()){
            int size = queue.size();
            rotten += size;
            if(rotten >= total) return time;
            time++;
            for(int i = 0; i < size; i++){
                int[] curr = queue.poll();
                for(int[] dir : directions){
                    int x = curr[0] + dir[0], y = curr[1] + dir[1];
                    if(x < 0 || y < 0 || x >= rows || y >= cols) continue;
                    if(grid[x][y] == 1){
                        grid[x][y] = 2;
                        queue.add(new int[]{x,y});
                    }
                }
            }
        }
        return -1;
    }
}
/*

st: 7:44 

    if(fresh is adj with rotten ) it will become rotten after a min.
    
    adj -> up, down, left, right 

    [[2,1,1]
    ,[1,1,0] -> after a min 
    ,[0,2,1]]
    
     [[2,2,1]
    ,[2,1,0] -> after a min 
    ,[0,1,1]]

    [[2,2,2]
    ,[2,2,0] -> after a min 
    ,[0,1,1]]

    add every rotten orage into the queue 
    int count = 0;
    while(!queue.isEmpty()){
        int size = queue.size();
        for(int i = 0; i < size: i++){
            curr = queue.poll();
            for(node n : curr.adj){
                if(n == 1){
                    visit(n);
                    queue.add(n);
                }
            }
        }
        count++;
    }
    return count;
    
    
    [2,1,1],
    [0,1,1]
    [1,0,1]]

*/
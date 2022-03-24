class Solution {
    public boolean isPrintable(int[][] targetGrid) {
        int m = targetGrid.length; 
        int n = targetGrid[0].length;
        
        Map<Integer,Color> colors = new HashMap<>();
        for(int i = 0; i < m ; i++){
            for(int j = 0;j < n; j++){
                int colVal = targetGrid[i][j];
                Color currCol = colors.getOrDefault(colVal, new Color(colVal));
                currCol.left = Math.min(currCol.left,j);
                currCol.right = Math.max(currCol.right,j);
                currCol.top = Math.min(currCol.top,i);
                currCol.bottom = Math.max(currCol.bottom,i);
                colors.put(colVal,currCol);
            }
        }
        
        Map<Integer,Set<Integer>> graph = new HashMap<>();
        int[] indegree = new int[62];
        
        for(int color : colors.keySet()){
            Color currColor = colors.get(color);
            Set<Integer> overlaps = graph.getOrDefault(color, new HashSet<>());
            for(int i = currColor.top; i <= currColor.bottom; i++){
                for(int j = currColor.left; j <= currColor.right; j++){
                    if(targetGrid[i][j] != color){
                        if(!overlaps.contains(targetGrid[i][j])){
                           overlaps.add(targetGrid[i][j]); 
                           indegree[targetGrid[i][j]]++; 
                        }
    
                    }
                }
            }
            graph.put(color,overlaps);

        }
        
        Queue<Integer> queue = new LinkedList<>();
        int visited = 0;
        for(int i = 0; i < indegree.length; i++) if(indegree[i] == 0 && colors.containsKey(i)) queue.add(i);
        
        while(!queue.isEmpty()){
            int curr = queue.poll();
            visited++;
            for(int adj : graph.get(curr)){
                if(--indegree[adj] == 0){
                    queue.add(adj);
                }
            }
        }
                           
        return visited == colors.keySet().size();
    }
}

class Color{
    int color;
    int left, right, top, bottom;
    public Color(int col){
        color = col;
        left = Integer.MAX_VALUE; 
        right = -1;
        top = Integer.MAX_VALUE;
        bottom = -1;
        
    }
    public int getWidth(){
        return right - left + 1;
    }
    
    public int getHeight(){
        return bottom - top + 1;
    }
    public int getArea(){
        return getWidth() * getHeight();
    }
}

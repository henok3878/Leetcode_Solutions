class Solution {
    public int findJudge(int n, int[][] trust) {
        boolean[] visited = new boolean[n + 1];
        
        for(int[] edge : trust) visited[edge[0]] = true;
        
        int potentialAns = -1;
        for(int i = 1; i < visited.length ; i++){
            if(visited[i] == false){
                potentialAns = i;
                break;
            }
        }
        visited = new boolean[n + 1];
        for(int[] edge : trust){
            if(edge[1] == potentialAns) visited[edge[0]] = true;
        }
        for(int i = 1; i <  visited.length ; i++){
            if(i != potentialAns && visited[i] == false) return -1;
        }
        return potentialAns;
        
    }
}

/*
    trust[i] = [ai, bi] => ai trusts the person lableled bi (ai -> bi)
    

*/
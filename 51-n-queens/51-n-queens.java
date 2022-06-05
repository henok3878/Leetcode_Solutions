class Solution {

    public List<List<String>> solveNQueens(int n) {

        List<List<String >> list = new ArrayList<>();

        char[][] ch = new char[n][n];

        

        for(char[] c: ch)

            Arrays.fill(c, '.');

        

        solve(list, ch, n, 0);

        return list;

    }   

    public static void solve(List<List<String >> list, char[][] ch, int n, int c) {

        if (c == n) {

            List<String> res = new ArrayList<String>();

            

            for(int i = 0; i < ch.length; i++) 

                res.add(new String(ch[i]));

            

            list.add(res);

            return;

        }

        

        for(int i = 0; i < n; i++) {                             

            if(isSafe(ch, i, c)) {

                ch[i][c] = 'Q';

                solve(list, ch, n, c + 1);

                ch[i][c] = '.';

            }

        }

    }

    public static boolean isSafe(char[][] ch, int r, int c) {

        for(int i = 0; i < ch.length; i++) 

            for(int j = 0; j < c; j++) 

                if(ch[i][j] == 'Q' && (r + j == c + i || r + c == i + j || r == i))

                    return false;

        return true;

    }

}



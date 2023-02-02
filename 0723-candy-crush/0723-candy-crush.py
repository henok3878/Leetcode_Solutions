class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        
        """
        -> crush all at the same time. 
            (tricky)
            - go throght the board once and mark every thing that is crushable 
        -> push every thing down. 
        
         0 1 
         1 0
         1 0
        >1 1 1 1
         ^
        """
        n = len(board) # rows 
        m = len(board[0]) # cols 
            
        def return_crushable_cell():
            crushable = set()
            for i in range(n):
                for j in range(m):
                    if board[i][j] == 0:
                        continue 
                    if i + 2 < n and board[i][j] == board[i + 1][j] and board[i + 1][j] == board[i + 2][j]:
                        crushable |= {(i,j), (i + 1, j) , (i + 2, j) } 
                    if j + 2 < m and board[i][j] == board[i][j + 1] and board[i][j + 1] == board[i][j + 2]:
                        crushable |= {(i,j), (i, j + 1) , (i,j + 2)} 
            return crushable 
        
        def drop_crushed_cell(crushable):
            for col in range(m):
                bottom_cell = n - 1 
                for row in range(n-1,-1,-1):
                    if (row, col) not in crushable:
                        board[bottom_cell][col] = board[row][col] 
                        bottom_cell -= 1 
                for row in range(bottom_cell + 1):
                    board[row][col] = 0 
                        
            
        def play():
            while True:
                crushable = return_crushable_cell() 
                if not crushable:
                    break 
                drop_crushed_cell(crushable)
        
        play() 
        return board 
        
            
            
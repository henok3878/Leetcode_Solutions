class Solution:
    def isValidSudoku(self, grid: List[List[str]]) -> bool:
        n = len(grid) # num of rows 
        m = len(grid[0]) # num of cols
        
        def get_kth_bit(x, k):
            return (x >> k) & 1
        def set_kth_bit(x, k):
            return x | ( 1 << k)
            

        def is_subgrid_valid(x,y): 
            '''
            Given the start of the subgrid, returns True if it's valid False otherwise. 
            '''
            seen = [False] * 10
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    if grid[i][j] != '.':
                        val = int(grid[i][j]) 
                        if seen[val]:
                            return False 
                        seen[val] = True 
            return True 
        
        for i in range(0,n,3):
            for j in range(0, m, 3):
                if not is_subgrid_valid(i,j):
                    return False 
        cols_info = [0 for _ in range(m)]
        for i in range(n):    
            curr_row = [False] * 10 
            for j in range(m):
                if grid[i][j] != '.':
                    val = int(grid[i][j]) 
                    if curr_row[val] or get_kth_bit(cols_info[j],val):
                        return False 
                    cols_info[j] = set_kth_bit(cols_info[j], val)
                    curr_row[val] = True 
        return True 





"""
does jth col, has x? 

m * 10 grid 


Given sudoko board, check if it's valid. 
    - Valid:
        - 1-9 in a row but no duplicate  
        - 1-9 in a col but non duplicate 
        - same for 3x3 boxes 

[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

Clarifications? 
- Do we consider all 3x3 boxes? for example this one TL: 2,2 -> BR: 4,4
    No
- we don't have have all the digits in a row, col, subgrid, right? 
    Yes
- Should I assume all the iinputs has size 9x9? Yes

Approaches:
    1: Brute Force:
        - For each cell (i, j), 
            - Validate ith row:
            - Validate jth col: 
        - For each subgrid, validate
            - 
    2. 
        - Iterate over the board while storing visited (already seen) values for curr row and all the cols
            - if curr value is seen, return False 
        - validate subgrid 

Implementation: 
- is_subgrid_valid(x,y):

"""

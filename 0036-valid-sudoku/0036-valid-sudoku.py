class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def check(i, row = False):
            seen = [0] * 10
            for j in range(9):
                cell = board[i][j] if row else board[j][i]
                if cell == ".":
                    continue
                cell = int(cell)
                seen[cell] += 1 
                if seen[cell] > 1:
                    return False 
            return True 
        
        def check_sub_box(x,y):
            seen = [0] * 10 
            for i in range(3):
                for j in range(3):
                    cell = board[x + i][y + j] 
                    if cell == ".":
                        continue 
                    cell = int(cell)

                    seen[cell] += 1 
                    if seen[cell] > 1:
                        return False 
            return True 
        
        for i in range(9):
            if (not check(i)) or (not check(i, True)):
                # print("First")
                return False 
            if (i % 3 == 0):
                if (not check_sub_box(0,i)) or (not check_sub_box(3, i)) or (not check_sub_box(6, i)):
                    # print("Second")
                    return False 
        return True
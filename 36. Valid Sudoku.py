Question:
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition. Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.    












Solution:
Visualization of the index (mod(i, 3), mod(j, 3)) for valid Sudoku :

0  0  0 | 1  1  1 | 2  2  2
0  0  0 | 1  1  1 | 2  2  2
0  0  0 | 1  1  1 | 2  2  2
--------+---------+---------
3  3  3 | 4  4  4 | 5  5  5
3  3  3 | 4  4  4 | 5  5  5
3  3  3 | 4  4  4 | 5  5  5
--------+----------+--------
6  6  6 | 7  7  7 | 8  8  8
6  6  6 | 7  7  7 | 8  8  8
6  6  6 | 7  7  7 | 8  8  8    

https://www.youtube.com/watch?v=TjFXEUCMqI8

class Solution:
    def isValidSudoku(self, board: List[List[str]])->bool:
        
        cols=collections.defaultdict(set)
        rows=collections.defaultdict(set)
        squares=collections.defaultdict(set) # key = (r/3, c/3)
        
        for r in range(9):
            for c in range(9):
                if board[r][c]==".": # if empty we dont care
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[r] or 
                    board[r][c] in squares[r//3,c//3]) : # it's a duplicate
                    
                    return False
                
                cols[c].add(board[r][c])
                rows[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
                
                
        return True # there has been no duplicates
                

    



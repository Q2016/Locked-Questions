Question:
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition. Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.    


Solution:
Visualization of the index k = i / 3 * 3 + j / 3 :

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

    def isValidSudoku(board)
    
        used1[9][9] = {0} #check each row
        used2[9][9] = {0} #check each column
        used3[9][9] = {0} #check each sub-boxes
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (board[i][j] != '.'):
                    num = int(board[i][j])
                    k = i / 3 * 3 + j / 3 # This gives the index of the matrix below
                    if (used1[i][num] or used2[j][num] or used3[k][num]):
                        return false
                    used1[i][num] = used2[j][num] = used3[k][num] = 1
        
        return true
    



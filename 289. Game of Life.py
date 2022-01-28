Question:
The board is made up of cells, where each cell has an initial state: live ~1 or dead~0. Each cell interacts with its eight neighbors
using the following four rules: Any live cell with fewer than two live neighbors dies (under-population). Cell with two or three 
live neighbors are not changed. Cell with more than three live neighbors dies. Dead cell with exactly three live neighbors becomes alive.
Return the next state.

Example 1:
Input: board = [[0,1,0],    =>     [0,0,0]
                [0,0,1],           [1,0,1]
                [1,1,1],           [0,1,1]
                [0,0,0]]           [0,1,0]
   


Solution: Brute force
The key point is to understand that the change to a cell is only decided by its nearby 8 cell in the original grid.
we should not use the updated cell to compute to change decision for other cell,therefore, the brute force way is to store 
the result in a new grid,then assign result back. But usually it requires use O(1) space, so the problem becomes: 
How can we store store the middle result without use extra space. The solution is to store the result in the origin grid as 
different number by some rule, so when we compute decision for other cell, we can know the original value of those nearby cell 
which has already been updated based on the rule. For example, we can do like this
living cells nearby | change | new value
            <2        1->0     2
            2,3       1->1     1
            >3        1->0     2
            3         0->1     3
so when we count living cells nearby, we need to count those value equals to 1 and 2

    def gameOfLife(self, board):
        if not board or len(board[0]) == 0:
            return
        m, n = len(board), len(board[0])
        for i, row in enumerate(board):
            for j, ele in enumerate(row):
                count = 0
                for a in xrange(max(0, i - 1), min(i + 2, m)):
                    for b in xrange(max(0, j - 1), min(j + 2, n)):
                        if (a, b) != (i, j) and 1 <= board[a][b] <= 2:
                            count += 1
                if board[i][j] == 0:
                    if count == 3:
                        board[i][j] = 3
                else:
                    if count < 2 or count > 3:
                        board[i][j] = 2
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1

                
                
# Time:  O(m * n)
# Space: O(1)                

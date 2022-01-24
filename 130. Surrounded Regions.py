Question:

Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:
Input: board = [["X","X","X","X"],
                ["X","O","O","X"],
                ["X","X","O","X"],
                ["X","O","X","X"]]
Output: [["X","X","X","X"],
         ["X","X","X","X"],
         ["X","X","X","X"],
         ["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border 
of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on 
the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

Solution: DFS, BFS

class Solution(object):
    # DFS
    def solve1(self, board):
        if not board or not board[0]:
            return 
        for i in [0, len(board)-1]:
            for j in range(len(board[0])):
                self.dfs(board, i, j)   
        for i in range(len(board)):
            for j in [0, len(board[0])-1]:
                self.dfs(board, i, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '.':
                    board[i][j] = 'O'
                
    def dfs(self, board, i, j):
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'O':
            board[i][j] = '.'
            self.dfs(board, i+1, j)
            self.dfs(board, i-1, j)
            self.dfs(board, i, j+1)
            self.dfs(board, i, j-1)
                
    # BFS
    def solve(self, board):
        queue = collections.deque([])
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r in [0, len(board)-1] or c in [0, len(board[0])-1]) and board[r][c] == "O":
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            if 0<=r<len(board) and 0<=c<len(board[0]) and board[r][c] == "O":
                board[r][c] = "."
                queue.extend([(r-1, c),(r+1, c),(r, c-1),(r, c+1)])
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == ".":
                    board[r][c] = "O"

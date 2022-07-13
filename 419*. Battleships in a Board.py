Question:
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.
Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the 
shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or 
vertical cell separates between two battleships (i.e., there are no adjacent battleships).
Follow up: Can you do it without modifying the board?
  
Example 1:
Input: board = [["X",".",".","X"], Output: 2  
                [".",".",".","X"],
                [".",".",".","X"]]
  
  
  
  
  
  

  
  
First I thought it's the number of islands. I think BFS makes more sence since wee only need to check close by neighbors.  
  
Solution:

  https://www.youtube.com/watch?v=gKhvVHd8ihI
  
class Solution:
  def countBattleships(self, board):
    
    def dfs(cur_i, cur_j):
      board[cur_i][cur_j]='.' # so that we have visited before
      
      for d in directions:
        new_i=cur_i+d[0]
        new_j=cur_j+d[1]
        
        if 0<=new_i<m and 0<=new_j<n and board[new_i][new_j]=='X':
          dfs(new_i, new_j)
    
    
    ans=0
    m=len(board)
    n=len(board[0])
    
    direction=[(-1,0),(1,0),(0,-1),(0,1)]
    
    for i in range(m):
      for j in range(n):
        if board[i][j]=='X':
          ans+=1
          dfs(i,j)
          
Time O(m*n+nums of X) I think it should be only nums of X because we visit only X      

Follow up:
  
  
ans=0
m=len(board)
n=len(board[0])

for i in range(m):
  for j in range(n):
    if board[i][j]=='X':
      if j>0 and board[i][j-1]=='X':
        contiue
      if i>0 and board[i-1][j]=='X':
        continue
        
      if j==0 or board[i][j-1]=='.':
        ans+=1
      if i=0 or board[i-1][j]=='.':
        ans+=1
        
 return ans

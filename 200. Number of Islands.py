Question:
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all 
four edges of the grid are all surrounded by water.

Example 1:
Input: 
  grid = [["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]]
Output: 1  
  
  
  
  
  
  
  
  
  
  
  
  
  
Solution: DFS
  
def numIslands(self, grid):
    if not grid:
        return 0
        
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                self.dfs(grid, i, j)
                count += 1
    return count

  
def dfs(self, grid, i, j):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
        return
      
    # What's usually called sink the island '#'
    # As in visited but optimized so we dont creat a matrix of visted =[False, True, etc]
    # https://leetcode.com/problems/number-of-islands/discuss/56349/7-lines-Python-~14-lines-Java
    grid[i][j] = '#' 
    self.dfs(grid, i+1, j)
    self.dfs(grid, i-1, j)
    self.dfs(grid, i, j+1)
    self.dfs(grid, i, j-1)  

    
# BFS:

from collections import deque
class Solution:
    def numIslands(self, grid):
        count = 0
        queue = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = 0
                    queue.append((i,j))
                    self.helper(grid,queue) # turn the adjancent '1' to '0'
                    count += 1
        print(grid)
        return count
    
    def helper(self,grid,queue):
        while queue:
            I,J = queue.popleft()
            for i,j in [I-1,J],[I+1,J],[I,J-1],[I,J+1]:
                if 0<= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    queue.append((i,j))
                    grid[i][j] = 0 #0
                    
                    
Time complexity DFS vs. BFS:
  Apart from what others have explained, there is one more benefit to using BFS for this problem. For DFS the space complexity is O(mn) 
  because in worst case we could have a input 2d matrix in which each point is land so the entire mn matrix is 1 big island and hence your 
  stack will be of size m*n. for BFS the queue will actually be O(min(m, n)) because in worst case where the grid is filled with lands, the 
  size of queue can grow up to min(M,N).

    
    

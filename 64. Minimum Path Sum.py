
https://leetcode.com/problems/minimum-path-sum/discuss/584967/Python-Grid-reduction-(Sounds-fancy-but-a-simple-method)-no-additional-space
  

Let's think of this problem in a super simple manner.

One important thing to remember is you can only walk right and down.
Notation I am going to use (row, column).

We are going to walk over the cells (the two for loops in the code). And each time we step 
on a cell, we are going to ask a question to ourself, how can I get to this cell with minimum 
sum from the previous step? Well, for the first cell (0,0) we don't need to do anything, right?

Next, think of walking over cell (0,1). What is the minimum sum to get to this cell? Well, it 
is too simple, just add the current number in the cell with the number of the cell on the left 
(for the case of (0,1) add it with the number in (0,0). This behavior is same for all the cells 
 in the topmost row.

Now, we get to the second row, we ask the same qustion for the cell in (1,0). How can we get here 
 with minimum sum? This is too simple, add the number in (1,0) with (0,0). But now, when we get to 
 (1,1), we have to add the number in (1,1) with minimum number from the cell above and the cell on 
 the left. By this time, your cell above and the one on the left already contains the minimum sum 
 path up to that cell. How conveninet, right? ^_^

That's all you gotta do. And whenever you step on the cell, update the cell accordingly.

We don't even need to use any additional space, we will overwrite stuff in the original grid. Why 
 can we do this? We can do this since we are processing the grid and every point that we are currently 
 reaching at bascially has the minimum sum up to that cell. We are accumulating the minimum sum path as 
 we walk over the grid.

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) <= 0 or grid is None:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if r==0 and c==0: # We just want to skip the top-left corner of the grid
                    continue
                if r-1<0: # Cases for elements in top row
                    grid[r][c] = grid[r][c] + grid[r][c-1]  
                elif c-1<0: # Cases for elements in leftmost column
                    grid[r][c] = grid[r][c] + grid[r-1][c]  
                else: # Normal cell
                    grid[r][c] = grid[r][c] + min(grid[r-1][c], grid[r][c-1])               
        
        return grid[rows-1][cols-1] # We have got the minimum path accumaled at the bottom-right corner, just return this

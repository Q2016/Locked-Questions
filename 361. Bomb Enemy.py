Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note that you can only put the bomb at an empty cell.
Example:
For the given grid
0 E 0 0
E 0 W E
0 E 0 0
return 3. (Placing a bomb at (1,1) kills 3 enemies)

Solution:
  First naive approach: just go through each location. If it’s 0, count ‘E’ in current row and column between ‘W’. If it’s E, or W, do nothing and move forward.
The problem here is: while we scan each element in the same row, we calculate how many ‘E’ in this row n times (assume n is the number of columns). To save time, we simply store the calculation in a variable every time we scan the first element in a new row. But be careful about the ‘W’. After we hit the ‘W’, we need to recount ‘E’ and update the variable.
The same approach applies to each column. Since we are scanning through each row, we jump from one column to another column. So we need an array to store ‘E’ counts for each column.
With those two auxiliary storages, we can just update the max ‘E’ counts when we encounter ‘0’ every time.
The code looks like this (Thanks to StefanPochmann’s solution)

My Solution:
  
  
  
  
  
  
  
  
  
 



https://medium.com/@rebeccahezhang/361-bomb-enemy-1b4b36d5a47a
class Solution {
    public int maxKilledEnemies(char[][] grid) {
        // iterate through the matrx by i(row), j(column) 
        // if it's '0', update the max so far by compare the current max and  
        // (enemies number in current row + enemies number in current column)
        // Becareful the grid.length == 0 should be the first thing to check
        // in case of array out of bound exception happens on grid[0].length
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0;
        }
        
        int m = grid.length;
        int n = grid[0].length;
        int max = 0;
        int rowCount = 0;
        int[] colCount = new int[n];
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // start from first row, count the enemies in the current row between two walls
                // store it to avoid recompute
                if (j == 0 || grid[i][j-1] == 'W') {
                    rowCount = 0;
                    for (int k = j; k < n && grid[i][k] != 'W'; k++) {
                        if (grid[i][k] == 'E') rowCount++;
                    }
                }
                // start from solumn, count the enemies in the current col between two walls
                if (i == 0 || grid[i-1][j] == 'W') {
                    colCount[j] = 0;
                    for (int k = i; k < m && grid[k][j] != 'W'; k++) {
                        if (grid[k][j] == 'E') colCount[j]++;
                    }
                }
                // if this is a position to place the bomb, get the current max
                if (grid[i][j] == '0') {
                    max = Math.max(max, rowCount + colCount[j]);
                }
            }
        }
        return max;
    }
}


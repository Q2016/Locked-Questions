Question:
There is a city composed of n x n blocks, where each block contains a single building shaped like a vertical square prism. You are given a 
0-indexed n x n integer matrix grid where grid[r][c] represents the height of the building located in the block at row r and column c.
A city's skyline is the the outer contour formed by all the building when viewing the side of the city from a distance. The skyline from each 
cardinal direction north, east, south, and west may be different.
We are allowed to increase the height of any number of buildings by any amount (the amount can be different per building). The height of a 0-height 
building can also be increased. However, increasing the height of a building should not affect the city's skyline from any cardinal direction.
Return the maximum total sum that the height of the buildings can be increased by without changing the city's skyline from any cardinal direction.

Example 1:
Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35
Explanation: The building heights are shown in the center of the above image.
The skylines when viewed from each cardinal direction are drawn in red.
The grid after increasing the height of buildings without affecting skylines is:
gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]


Solution: Row and Column Maximums [Accepted]
The skyline looking from the top is col_maxes = [max(column_0), max(column_1), ...]. 
Similarly, the skyline from the left is row_maxes [max(row_0), max(row_1), ...]

In particular, each building grid[r][c] could become height min(max(row_r), max(col_c)), 
and this is the largest such height. If it were larger, say grid[r][c] > max(row_r), then 
the part of the skyline row_maxes = [..., max(row_r), ...] would change.

These increases are also independent (none of them change the skyline), so we can perform them independently.

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        row_maxes = [max(row) for row in grid]
        col_maxes = [max(col) for col in zip(*grid)]

        return sum(min(row_maxes[r], col_maxes[c]) - val
                   for r, row in enumerate(grid)
                   for c, val in enumerate(row))
                   

        
        
Complexity Analysis
Time Complexity: O(N^2), where N is the number of rows (and columns) of the grid. We iterate through every cell of the grid.
Space Complexity: O(N), the space used by row_maxes and col_maxes.                   

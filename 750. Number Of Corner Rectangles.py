Question:
Given a grid where each entry is only 0 or 1, find the number of corner rectangles.
A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rectangle.
Note that only the corners need to have the value 1. Also, all four 1s used must be distinct.

Example 1:
Input: grid = 
[[1, 0, 0, 1, 0],
 [0, 0, 1, 0, 1],
 [0, 0, 0, 1, 0],
 [1, 0, 1, 0, 1]]
Output: 1
Explanation: There is only one corner rectangle, with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].


        
        
        

Solution:        
        
One straight-forward solution is: we can iterate any two rows, say r1 and r2, 
and for every column, we check if grid[r1][c] == grid[r2][c]. IF yes, we increate 
the count by 1. Then the number of rentangles formed by these two rows are
count * (count - 1) / 2.


https://sugarac.gitbooks.io/facebook-interview-handbook/content/number-of-corner-rectangles.html
public int countCornerRectangles(int[][] grid) {
        int ans = 0;
        for (int i = 0; i < grid.length - 1; i++) {
            for (int j = i + 1; j < grid.length; j++) {
                int counter = 0;
                for (int k = 0; k < grid[0].length; k++) {
                    if (grid[i][k] == 1 && grid[j][k] == 1) counter++;
                }
                if (counter > 0) ans += counter * (counter - 1) / 2;
            }
        }
        return ans;
    }


https://github.com/ShiqinHuo/LeetCode-Python/blob/master/Python/number-of-corner-rectangles.py
class Solution(object):
    def countCornerRectangles(self, grid):

        rows = [[c for c, val in enumerate(row) if val]
                for row in grid]
        result = 0
        for i in xrange(len(rows)):
            lookup = set(rows[i])
            for j in xrange(i):
                count = sum(1 for c in rows[j] if c in lookup)
                result += count*(count-1)/2
        return result


Time:  O(n * m^2), n is the number of rows with 1s, m is the number of cols with 1s
Space: O(n * m)

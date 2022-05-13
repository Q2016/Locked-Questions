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


class Solution {
 public:
  int countCornerRectangles(vector<vector<int>>& grid) {
    int ans = 0;

    for (int row1 = 0; row1 < grid.size() - 1; ++row1)
      for (int row2 = row1 + 1; row2 < grid.size(); ++row2) {
        int count = 0;
        for (int j = 0; j < grid[0].size(); ++j)
          if (grid[row1][j] && grid[row2][j])
            ++count;
        ans += count * (count - 1) / 2;
      }

    return ans;
  }
};

we can reduce time by increasing space complexity:
 
class Solution {
public:
    int countCornerRectangles(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size(), res = 0;
        for (int i = 0; i < m - 1; i++) { 
            vector<int> ones;
            for (int k = 0; k < n; k++) if (grid[i][k]) ones.push_back(k);
            for (int j = i + 1; j < m; j++) {
                int cnt = 0;
                for (int l = 0; l < ones.size(); l++) {
                    if (grid[j][ones[l]]) cnt++;
                }
                res += cnt * (cnt - 1) / 2;
            }           
        }
        return res;
    }
};


Time:  O(n * m^2), n is the number of rows with 1s, m is the number of cols with 1s
Space: O(n * m)

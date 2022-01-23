Question:
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount 
of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once and Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 
Example 1:
Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7. 
  
  
  
Solution: DFS


int dfs(vector<vector<int>>& g, int i, int j) {
  if (i < 0 || j < 0 || i >= g.size() || j >= g[i].size() || g[i][j] <= 0)  return 0;
  g[i][j] = -g[i][j];//mark as visited
  auto res = max({ dfs(g, i + 1, j), dfs(g, i, j + 1), dfs(g, i - 1, j), dfs(g, i, j - 1) });
  g[i][j] = -g[i][j];//back track
  return g[i][j] + res;
}

int getMaximumGold(vector<vector<int>>& grid, int res = 0) {
  for (auto i = 0; i < grid.size(); ++i)
    for (auto j = 0; j < grid[i].size(); ++j)
      res = max(res, dfs(grid, i, j));
  return res;
}

        


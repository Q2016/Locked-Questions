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
  
  
  
  
  
  
  
  
  
  
  
  
  
Solution: Backtracking


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

Each of the k gold cells can at most have 4 neighbors. Therefore,
Time: O(k * 4 ^ k + m * n - k), space: O(m * n), where k = number of gold cells, m = grid.length, n = grid[0].length.





BFS
Some said we can NOT use BFS to solve this problem, I do NOT believe and write a BFS code.:P

Assume there are k cells containing gold. Use 0 ~ k - 1 to identify the gold cells; Since k <= 25, we can set 0th ~ (k - 1)th bit of an int to record the trace of the correspoinding cell in a path; e.g., in example 1,

[[0,6,0],
 [5,8,7],
 [0,9,0]]
the id of gold cell (0, 1) and (1, 1) are 0 and 2 respectively. The one cell trace of them are 1 (1 << 0) and 4 (1 << 2); The trace of of the path including only the two cells is 1 | 4 = 5, and the sum of the path is 6 + 8 = 14.

Loop through the grid, for each gold cell put into a Queue the coordinate (i, j), gold value grid[i][j], and the trace (1 << goldCellId), then perform BFS to get the max value;
For any gold cell neighbor (r, c) during BFS, ignore it if it is already in the trace ((trace & oneCellTrace[r][c]) != 0); otherwise, add its one cell trace to the current trace (trace | oneCellTrace[r][c]).

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n, q, goldCellId, ans = len(grid), len(grid[0]), [], 0, 0
        oneCellTrace = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    oneCellTrace[i][j] = 1 << goldCellId
                    goldCellId += 1
                    q.append((i, j, grid[i][j], oneCellTrace[i][j]))
        for i, j, sum, trace in q:
            ans = max(sum, ans)
            for r, c in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if r >= 0 and r < m and c >= 0 and c < n and grid[r][c] and not (trace & oneCellTrace[r][c]):
                    q.append((r, c, grid[r][c] + sum, trace | oneCellTrace[r][c]))
        return ans
       
Time & space: O(k * 4 ^ k + m * n - k), where k = number of gold cells, m = grid.length, n = grid[0].length.       

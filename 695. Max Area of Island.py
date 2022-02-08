Question:
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally 
(horizontal or vertical.) You may assume all four edges of the grid are surrounded by water. The area of an island is the number 
of cells with a value 1 in the island. Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
               [0,0,0,0,0,0,0,1,1,1,0,0,0],
               [0,1,1,0,1,0,0,0,0,0,0,0,0],
               [0,1,0,0,1,1,0,0,1,0,1,0,0],
               [0,1,0,0,1,1,0,0,1,1,1,0,0],
               [0,0,0,0,0,0,0,0,0,0,1,0,0],
               [0,0,0,0,0,0,0,1,1,1,0,0,0],
               [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.    

Solution: DFS
The solution is to search each island. Remember marking grid[r][c] = 2 as visited. The idea is to count the area of each island using dfs. 
During the dfs, we set the value of each point in the island to 0. 

    def maxAreaOfIsland(grid) :
        m = grid.size() 
        n = grid[0].size(), 
        ans = 0;
        for (int i = 0; i < m; i++) 
            for (int j = 0; j < n; j++) 
                if (grid[i][j] == 1): ans = max(ans, dfs(grid, i, j));
        return ans;
    
    def dfs(grid, row, col):
        m = grid.size(), 
        n = grid[0].size(), 
        area = 1;
        grid[row][col] = 2;
        dir=[-1,0,1,0,-1]
        for (int i = 0; i < 4; i++):
            r = row+dir[i]
            c = col+dir[i+1]
            if (r >= 0 && r < m && c >= 0 && c < n && grid[r][c] == 1): 
                area += dfs(grid, r, c);    
        return area;
    

The time complexity is O(mn).

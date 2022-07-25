Question:
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below). The robot can only move either down or 
right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be? An obstacle and space is marked as 1 and 0 
respectively in the grid.

Example 1:
Input: obstacleGrid = [[0,0,0],
                       [0,1,0],
                       [0,0,0]]
Output: 2, Explanation: There is one obstacle in the middle of the 3x3 grid above. There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down    2. Down -> Down -> Right -> Right    









No link, but I think very similar

Solution:
Well, this problem is similar to Unique Paths. The introduction of obstacles only changes the boundary conditions and make some points 
unreachable (simply set to 0). Denote the number of paths to arrive at point (i, j) to be P[i][j], the state equation is 
P[i][j] = P[i - 1][j] + P[i][j - 1] if obstacleGrid[i][j] != 1 and 0 otherwise. Now let's finish the boundary conditions. In the Unique Paths 
problem, we initialize P[0][j] = 1, P[i][0] = 1 for all valid i, j. Now, due to obstacles, some boundary points 
are no longer reachable and need to be initialized to 0. For example, if obstacleGrid is like [0, 0, 1, 0, 0], then the last three points are 
not reachable and need to be initialized to be 0. The result is [1, 1, 0, 0, 0].
Note that we pad the obstacleGrid by 1 and initialize dp[0][1] = 1 to unify the boundary cases.

    def uniquePathsWithObstacles(obstacleGrid):
        m = obstacleGrid.size() 
        n = obstacleGrid[0].size()
        # dp [m + 1][n + 1]        
        dp[0][1] = 1;
        for (int i = 1; i <= m; i++)
            for (int j = 1; j <= n; j++)
                if (!obstacleGrid[i - 1][j - 1])
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
        return dp[m][n];
    

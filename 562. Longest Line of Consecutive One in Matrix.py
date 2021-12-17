Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.

Example:

Input:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]
Output: 3
 

We can also consider using the DP solution, we build a three-dimensional DP array, 
where DP [i] [j] [k] is used to traverse the number NUMS [i] [j] from the beginning, 
and the row of rings 1 The number of K, the value of K is 0, 1, 2, 3,
The four situations corresponding to level, vertical, diagonal, and reverse angle. 
Then the process of updating the DP array, if the number is jumped directly, then the 
horizontal direction adds the previous DP value, plus the top vertical direction
A number of DP values, the diagonal direction plus the DP value of the number in the 
upper right, and the reverse diagonal plus the DP value of the upper left number, then 
each value is used to update the result RES, see the code as follows:

  
  
 class Solution2 {
     int longestLine(int[][] M) {
         if (M == null || M.length == 0 || M[0].length == 0) return 0;
         int m = M.length, n = M[0].length, res = 0;
         int[][][] dp = new int[m][n][4];
         for (int i = 0; i < m; ++i) {
             for (int j = 0; j < n; ++j) {
                 if (M[i][j] == 0) continue;
                 for (int k = 0; k < 4; ++k) dp[i][j][k] = 1;
                 if (j > 0) dp[i][j][0] += dp[i][j - 1][0]; // horizonal
                 if (i > 0) dp[i][j][1] += dp[i - 1][j][1]; // vertical
                 if (i > 0 && j < n - 1) dp[i][j][2] += dp[i - 1][j + 1][2]; // diagonal
                 if (i > 0 && j > 0) dp[i][j][3] += dp[i - 1][j - 1][3]; // anti-diagonal
                 res = Math.max(res, Math.max(dp[i][j][0], dp[i][j][1]));
                 res = Math.max(res, Math.max(dp[i][j][2], dp[i][j][3]));
             }
         }
         return res;
     }
 }

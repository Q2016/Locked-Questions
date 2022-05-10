Question:
Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.

Example:
Input:     , Output: 3
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]









Solution: DP
We use DP solution, we build a three-dimensional DP array, where DP[i][j][k] is used to traverse 
the matrix M[i][j]. Value of K is 0, 1, 2, 3. The four situations corresponding to level, vertical, diagonal, and reverse angle. 

     def longestLine(M) :
         if (M == None or M.size() == 0 or M[0].size() == 0) :
             return 0
         m = M.size() 
         n = M[0].size() 
         res = 0
         #dp = initialize matrix of int[m][n][4]
         for i in range(m) : 
             for j in range(n) :
                 if (M[i][j] == 0) continue;
                 for k in range(4): dp[i][j][k] = 1
                 if (j > 0): dp[i][j][0] += dp[i][j - 1][0] # horizonal
                 if (i > 0) dp[i][j][1] += dp[i - 1][j][1]; # vertical
                 if (i > 0 and j < n - 1) : dp[i][j][2] += dp[i - 1][j + 1][2] # diagonal
                 if (i > 0 and j > 0) : dp[i][j][3] += dp[i - 1][j - 1][3] # anti-diagonal
                 res = max(res, max(dp[i][j][0], dp[i][j][1]))
                 res = max(res, max(dp[i][j][2], dp[i][j][3]))
         return res
     

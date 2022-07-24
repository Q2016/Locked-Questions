Question:
Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.

Example:
Input:     , Output: 3
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]









Solution: DP
 
https://www.youtube.com/watch?v=eWweg7QwB6A
     
     
class Solution:
  def longestLine(self, M):
     if not M:
        return 0
     
     m=len(M)
     n=len(M[0])
     
     dp=[[(0,0,0,0)]*(n+2) for _ in range(m+1)]
     ans=0
     
     for i in range(1, m+1):
        for j in range(1, n+1):
           if M[i-1][j-1]==1:
               dp[i][j]=(dp[i][j-1][0]+1, dp[i-1][j-1][1]+1,dp[i-1][j][2]+1, dp[i-1][j+1][3]+1)
               ans=max(ans, max(dp[i][j]))
            
     return ans

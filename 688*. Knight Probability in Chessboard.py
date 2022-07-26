Question:
On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The rows and columns are 0-indexed, 
so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1). A chess knight has eight possible moves it can make, as illustrated 
below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction. Each time the knight is to move, it chooses one 
of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there. The knight continues moving until 
it has made exactly k moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

Example 1:
Input: n = 3, k = 2, row = 0, column = 0
Output: 0.06250
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.    

Example 1:
Input: n = 3, k = 2, row = 0, column = 0
Output: 0.06250
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.






Solution: DP

     https://www.youtube.com/watch?v=hNovJsUbNjo
 
Time is O(N^2*K*8)
 Space is O(N^2*K*8)
 Top down
    
    
class Solution:
 
 def knightProbability(self, N, K, r ,c):
    
    def dp(cur_k, cur_r, cur_c):

       if (cur_k, cur_r, cur_c) in memo:
          return memo[(cur_k, cur_r, cur_c)]
       if cur_k==K:
          return 1
       ans=0
       for d in moves:
          new_r=cur_r+d[0]
          new_c=cur_c+d[1]

         if 0<=new_r<N and 0<=new_c<N:
            ans+=0.125*dp(cur_k+1, new_r, new_c)  # All probabilities are independent

       memo[(cur_k, cur_r, cur_c)]= ans

       return ans
     
    memo={}
    moves=((-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2))
    return dp(0, r, c)
    
    
Bottom up:
    
    
    
    
    
    
    
    
    
    
    Dynamic Programming

Let f[r][c][steps] be the probability of being on square (r, c) after a number of 'steps' steps. Based on how a knight moves, 
we have the following recursion:
f[r][c][steps] = \sum_{dr, dc} f[r+dr][c+dc][steps-1] / 8.0 
where the sum is taken over the eight (dr, dc)(dr,dc) pairs (2, 1),(2,1), (2, -1),(2,−1), 
(-2, 1),(−2,1), (-2, -1),(−2,−1), (1, 2),(1,2), (1, -2),(1,−2), (-1, 2),(−1,2), (-1, -2)(−1,−2).
Instead of using a three-dimensional array f, we will use two two-dimensional ones dp and dp2, storing 
the result of the two most recent layers we are working on. dp2 will represent f[][][steps], and dp 
will represent f[][][steps-1].


    def knightProbability(self, N, K, r, c):
        dp = [[0] * N for _ in xrange(N)]
        dp[r][c] = 1
        for _ in xrange(K):
            dp2 = [[0] * N for _ in xrange(N)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for dr, dc in ((2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)):
                        if 0 <= r + dr < N and 0 <= c + dc < N:
                            dp2[r+dr][c+dc] += val / 8.0
            dp = dp2

        return sum(map(sum, dp))

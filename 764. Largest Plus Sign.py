Solution from:
  Approach #2: Dynamic Programming [Accepted]
Intuition

How can we improve our bruteforce? One way is to try to speed up the inner loop involving k, the order of the candidate plus sign. 
If we knew the longest possible arm length L_u, L_l, L_d, L_r in each direction from a center, we could know the order 
min(L_u, L_l, L_d, L_r) of a plus sign at that center. We could find these lengths separately using dynamic programming.

Algorithm

For each (cardinal) direction, and for each coordinate (r, c) let's compute the count of that
coordinate: the longest line of '1's starting from (r, c) and going in that direction. With dynamic 
  programming, it is either 0 if grid[r][c] is zero, else it is 1 plus the count of the coordinate in 
  the same direction. For example, if the direction is left and we have a row like 01110110, the 
  corresponding count values are 01230120, and the integers are either 1 more than their successor, or 0. 
  For each square, we want dp[r][c] to end up being the minimum of the 4 possible counts. At the end, we 
  take the maximum value in dp.

  
  class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        banned = {tuple(mine) for mine in mines}
        dp = [[0] * N for _ in xrange(N)]
        ans = 0
        
        for r in xrange(N):
            count = 0
            for c in xrange(N):
                count = 0 if (r,c) in banned else count+1
                dp[r][c] = count
            
            count = 0
            for c in xrange(N-1, -1, -1):
                count = 0 if (r,c) in banned else count+1
                if count < dp[r][c]: dp[r][c] = count
        
        for c in xrange(N):
            count = 0
            for r in xrange(N):
                count = 0 if (r,c) in banned else count+1
                if count < dp[r][c]: dp[r][c] = count
            
            count = 0
            for r in xrange(N-1, -1, -1):
                count = 0 if (r, c) in banned else count+1
                if count < dp[r][c]: dp[r][c] = count
                if dp[r][c] > ans: ans = dp[r][c]
        
        return ans
  



Approach #1: Dynamic Programming [Accepted]
Intuition and Algorithm

Let f[r][c][steps] be the probability of being on square (r, c) after steps steps. 
Based on how a knight moves, we have the following recursion:

f[r][c][steps] = \sum_{dr, dc} f[r+dr][c+dc][steps-1] / 8.0f[r][c][steps]=\sum_{dr, dc} f[r+dr][c+dc][steps−1]/8.0

where the sum is taken over the eight (dr, dc)(dr,dc) pairs (2, 1),(2,1), (2, -1),(2,−1), 
(-2, 1),(−2,1), (-2, -1),(−2,−1), (1, 2),(1,2), (1, -2),(1,−2), (-1, 2),(−1,2), (-1, -2)(−1,−2).

Instead of using a three-dimensional array f, we will use two two-dimensional ones dp and dp2, storing 
the result of the two most recent layers we are working on. dp2 will represent f[][][steps], and dp 
will represent f[][][steps-1].


class Solution(object):
    def knightProbability(self, N, K, r, c):
        dp = [[0] * N for _ in xrange(N)]
        dp[r][c] = 1
        for _ in xrange(K):
            dp2 = [[0] * N for _ in xrange(N)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for dr, dc in ((2,1),(2,-1),(-2,1),(-2,-1),
                                   (1,2),(1,-2),(-1,2),(-1,-2)):
                        if 0 <= r + dr < N and 0 <= c + dc < N:
                            dp2[r+dr][c+dc] += val / 8.0
            dp = dp2

        return sum(map(sum, dp))

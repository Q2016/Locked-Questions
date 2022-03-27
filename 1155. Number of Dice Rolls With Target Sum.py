Question:
You have d dice, and each die has f faces numbered 1, 2, ..., f.
Return the number of possible ways (out of f^d total ways) to roll the dice so the sum of the face up numbers equals target.

Example 1:
Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.  
  
  
Solution:  DP

This problem is like 518. Coin Change 2, with the difference that the total number of coins (dices) should be equal to d.

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for i in range(target + 1)] for j in range(d + 1)]
        dp[0][0] = 1
        
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                k = 1
                while k <= min(j, f):
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) # k enters because of possible ways the outcome from a dice can appear
                    k += 1
        return dp[d][target] % mod

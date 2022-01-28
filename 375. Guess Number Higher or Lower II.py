Question:
We are playing the Guessing Game. The game will work as follows: I pick a number between 1 and n. You guess a number.
If you guess the right number, you win the game. If you guess the wrong number, then I will tell you whether the number 
I picked is higher or lower, and you will continue guessing. Every time you guess a wrong number x, you will pay x dollars. 
If you run out of money, you lose the game. Given a particular n, return the minimum amount of money you need to guarantee 
a win regardless of what number I pick.

Example 1:
Input: n = 10
Output: 16
Explanation: The winning strategy is as follows:
- The range is [1,10]. Guess 7.
    - If this is my number, your total is $0. Otherwise, you pay $7.
    - If my number is higher, the range is [8,10]. Guess 9.
        - If this is my number, your total is $7. Otherwise, you pay $9.
        - If my number is higher, it must be 10. Guess 10. Your total is $7 + $9 = $16.
        - If my number is lower, it must be 8. Guess 8. Your total is $7 + $9 = $16.
    - If my number is lower, the range is [1,6]. Guess 3.
        - If this is my number, your total is $7. Otherwise, you pay $3.
        - If my number is higher, the range is [4,6]. Guess 5.
            - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $5.
            - If my number is higher, it must be 6. Guess 6. Your total is $7 + $3 + $5 = $15.
            - If my number is lower, it must be 4. Guess 4. Your total is $7 + $3 + $5 = $15.
        - If my number is lower, the range is [1,2]. Guess 1.
            - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $1.
            - If my number is higher, it must be 2. Guess 2. Your total is $7 + $3 + $1 = $11.
The worst case in all these scenarios is that you pay $16. Hence, you only need $16 to guarantee a win.

    
Solution: Good example to understand Top down DP and Bottom up DP

Solution 1: Top down DP

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(None)
        def dp(left, right):
            if left >= right:
                return 0
            ans = math.inf
            for pick in range(left, right + 1):
                leftCost = dp(left, pick - 1) + pick  # Cost on the left side, if pivot is not a secret number
                rightCost = dp(pick + 1, right) + pick  # Cost on the right side, if pivot is not a secret number
                cost = max(leftCost, rightCost)  # The cost is the maximum between the left side and the right side
                ans = min(ans, cost)  # Choose pivot which will cause minimum cost
            return ans
        return dp(1, n)

Time: O(N^3)
Space: O(N^2)

    
✔️ Solution 2: Bottom up DP
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for l in range(n, 0, -1):
            for r in range(l + 1, n + 1):
                dp[l][r] = math.inf
                for pick in range(l, r + 1):
                    leftCost = dp[l][pick - 1] + pick  # Cost on the left side, if pivot is not a secret number
                    rightCost = dp[pick + 1][r] + pick  # Cost on the right side, if pivot is not a secret number
                    cost = max(leftCost, rightCost)  # The cost is the maximum between the left side and the right side
                    dp[l][r] = min(dp[l][r], cost)  # Choose pivot which will cause minimum cost
        return dp[1][n]


Time: O(N^3)
Space: O(N^2)    

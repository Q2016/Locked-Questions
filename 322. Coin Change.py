Question:
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1


Solution: Recursive Method
    
The idea is very classic dynamic programming: think of the last step we take. 
Suppose we have already found out the best way to sum up to amount a, then for the last step, 
we can choose any coin type which gives us a remainder r where r = a-coins[i] for all i's. 
For every remainder, go through exactly the same process as before until either the 
remainder is 0 or less than 0 (meaning not a valid solution). With this idea, the only 
remaining detail is to store the minimum number of coins needed to sum up to r so that 
we don't need to recompute it over and over again.

    def coinChange(self, coins, amount):

        rs = [amount+1] * (amount+1)
        rs[0] = 0
        for i in xrange(1, amount+1):
            for c in coins:
                if i >= c:
                    rs[i] = min(rs[i], rs[i-c] + 1)

        if rs[amount] == amount+1:
            return -1
        return rs[amount]

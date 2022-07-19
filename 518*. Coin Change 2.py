Question:
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1    
    
Solution:  DP
    
 https://www.youtube.com/watch?v=Mjy4hd2xgrs
 
Time O(n*M)
    
class Solution:
    def change(self, amount, coin):
        cach={}
        
        def dfs(i,a):
            if a==amount:
                return 1
            if a >amount:
                return 0
            if i==len(coins):
                return 0
            if (i,a) in cache:
                return cache[(i, a)]
            
            cache[(i,a)]=dfs(i,a+coins[i])+dfs(i+1,a)
            return cache[(i,a)]
        return dfs(0,0)
    
    
    
    
    
    
    
    
    
    
    
This is a classic knapsack problem. Honestly, I'm not good at knapsack problem, it's really tough for me.
dp[i][j] : the number of combinations to make up amount j by using the first i types of coins
State transition:
not using the ith coin, only using the first i-1 coins to make up amount j, then we have dp[i-1][j] ways.
using the ith coin, since we can use unlimited same coin, we need to know how many ways to make 
up amount j - coins[i-1] by using first i coins(including ith), which is dp[i][j-coins[i-1]]
Initialization: dp[i][0] = 1. Once you figure out all these, it's easy to write out the code:

    def change(amount, coins) :
        
        dp = [ [0]*(len(coins)+1) for i in range(amount+1)]
        dp[0][0] = 1
        
        for i in range(len(coins)):            
            dp[i][0] = 1;
            for j in range(1,amount+1):
                if j >= coins[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j] 
           
        return dp[len(coins)][amount]
    
Now we can see that dp[i][j] only rely on dp[i-1][j] and dp[i][j-coins[i]], then we can optimize the space by only using one-dimension array.

    def change(amount, coins) :
        dp = [0]*(amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin,amount+1) :
                dp[i] += dp[i-coin]
            
        return dp[amount]
    

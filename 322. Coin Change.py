Question:
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

    
    
    
    
    
    

Solution: Recursive Method
    
If you carefully observe the below 3 codes.
You will see that the DP Memoization is dervied from the Recursion code just by changing 3 lines and same is the case for DP Tabulation 
from Memoization.

Recursion

class Solution {
public:
    int recursion(vector<int> wt, int w, int n)
    {
        if (n == 0 || w == 0)
            return (w == 0) ? 0 : INT_MAX - 1;
        
        if (wt[n - 1] > w) 
            return 0 + recursion(wt, w - 0, n - 1);
        else 
            return min(0 + recursion(wt, w - 0, n - 1), 1 + recursion(wt, w - wt[n - 1], n));
    }
    
    int coinChange(vector<int>& coins, int amount) 
    {
        int minCoins = recursion(coins, amount, coins.size());
        return minCoins == INT_MAX - 1 ? -1 : minCoins;    
    }
};


DP Memoization

class Solution {
public:
    int dp[10000 + 1][12 + 1];  // New Line Added
    
    int memoization(vector<int>& wt, int w, int n)
    {
        if (n == 0 || w == 0)
            return (w == 0) ? 0 : INT_MAX - 1;
        
        if (dp[w][n] != -1) // New Line Added
            return dp[w][n];  // New Line Added
			
        if (wt[n - 1] > w) 
            return dp[w][n] = 0 + memoization(wt, w - 0, n - 1);
        else 
            return dp[w][n] = min(0 + memoization(wt, w - 0, n - 1), 1 + memoization(wt, w - wt[n - 1], n));
    }
    
    int coinChange(vector<int>& coins, int amount) 
    {
        memset(dp, -1, sizeof(dp)); // New Line Added
        int minCoins = memoization(coins, amount, coins.size());
        return minCoins == INT_MAX - 1 ? -1 : minCoins;    
    }
};


DP Tabulation

class Solution {
public:
    int dp[10000 + 1][12 + 1];
    
    int tabulation(vector<int> wt, int w, int n)
    {
        for (int i = 0; i < w + 1; i++)
            for (int j = 0; j < n + 1; j++)
                if (i == 0 || j == 0)
                    dp[i][j] = (i == 0) ? 0 : INT_MAX - 1;
        
        for (int i = 1; i < w + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                if (wt[j - 1] > i) 
                    dp[i][j] = 0 + dp[i - 0][j - 1];
                else 
                    dp[i][j] = min(0 + dp[i - 0][j - 1], 1 + dp[i - wt[j - 1]][j - 0]);
            }
        }
        
        return dp[w][n];
    }
    
    int coinChange(vector<int>& coins, int amount) 
    {
        memset(dp, -1, sizeof(dp));
        int minCoins = tabulation(coins, amount, coins.size());
        return minCoins == INT_MAX - 1 ? -1 : minCoins;    
    }
};

Complexity:
-First recursive approach, no memoization is used. each recursive call makes 2 other calls and those 2 calls each make their owen 2 recursive calls. 
so the time and space complexity is O(2^N).

-Second approach, since a 2d array is used to cache the results, we don't have to compute the same subproblem over and over again. 
so the total number of recursive calls is the total number of all possible states in the problem which is amountno of coins.so the 
space and time complexity are O(MN)

-THIRD approach, a 2d array is being created which has a space complexity of O(MN) and time complexity is traversing w+1 rows and n+1 columns 
which is O(MN).

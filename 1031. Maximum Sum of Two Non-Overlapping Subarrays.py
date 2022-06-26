Question:
Given an integer array nums and two integers firstLen and secondLen, return the maximum 
sum of elements in two non-overlapping subarrays with lengths firstLen and secondLen.
The array with length firstLen could occur before or after the array with length secondLen, 
but they have to be non-overlapping.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.    


Solution: prefix sum, related to buy/sell stocks III (First read Stock III below and then this answer)
 
 
buy/sell stock 2 times: 
Similar to Best Time to Buy and Sell Stock III, but instead of maximum profit, we track maximum sum of N elements.
Left-to-right, track the maximum sum of L elements in left. Right-to-left, track the maximum sum of M elements in right.
Then, find the split point where left[i] + right[i] gives us the maximum sum.
Note: we need to do it twice for (L, M) and (M, L).

int maxTwoNoOverlap(vector<int>& A, int L, int M, int sz, int res = 0) {
    vector<int> left(sz + 1), right(sz + 1);
    for (int i = 0, j = sz - 1, s_r = 0, s_l = 0; i < sz; ++i, --j) {
      s_l += A[i], s_r += A[j];
      left[i + 1] = max(left[i], s_l);
      right[j] = max(right[j + 1], s_r);
      if (i + 1 >= L) s_l -= A[i + 1 - L];
      if (i + 1 >= M) s_r -= A[j + M - 1];
    }
    for (auto i = 0; i < A.size(); ++i) {
      res = max(res, left[i] + right[i]);
    }
    return res;
}
int maxSumTwoNoOverlap(vector<int>& A, int L, int M) {
    return max(maxTwoNoOverlap(A, L, M, A.size()), maxTwoNoOverlap(A, M, L, A.size()));
}

       
       
123. Best Time to Buy and Sell Stock III:       
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most two transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).   

Example 1:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3. 




Naive Solution:
This solution is based on the Best Time to Buy and Sell Stock where you track the global min price and max profit. 
It's easier to come up with, but requires extra memory.

Go left to right, and store the best profit for each day individually in left
left[i] shows the max profit for days [1, i]
Go right to left, store best profit in right
right[i] shows the max profit for days [i + 1, n]
The maximum profit is the maximum of left[i] + right[i]

int maxProfit(vector<int>& prices) {
    int n = prices.size(), min_l = INT_MAX, max_r = 0, res = 0;
    vector<int> left(n + 1), right(n + 1);
    for (auto i = 0; i < n; ++i) {
      auto price_l = prices[i], price_r = prices[n - i - 1];
      min_l = min(min_l, price_l);
      max_r = max(max_r, price_r);
      left[i + 1] = max(left[i], price_l - min_l);
      right[n - i - 1] = max(right[n - i], max_r - price_r);
    }
    for (auto i = 0; i <= n; ++i) res = max(res, left[i] + right[i]);
    return res;
}
 
 
 
 
 
Python Solution is given below: (But we dont need it) 
 

Solution: 
It's not difficult to get the DP recursive formula:
dp[k, i] = max(dp[k, i-1], prices[i] - prices[j] + dp[k-1, j-1]), j=[0..i-1]
For k transactions, on i-th day,
if we don't trade then the profit is same as previous day dp[k, i-1];
and if we bought the share on j-th day where j=[0..i-1], then sell the share on i-th day then the profit is prices[i] - prices[j] + dp[k-1, j-1] .
Actually j can be i as well. When j is i, the one more extra item prices[i] - prices[j] + dp[k-1, j] = dp[k-1, i] looks like we just lose one chance 
of transaction.

I see someone else use the formula dp[k, i] = max(dp[k, i-1], prices[i] - prices[j] + dp[k-1, j]), where the last one is dp[k-1, j] instead of 
dp[k-1, j-1]. It's not the direct sense, as if the share was bought on j-th day, then the total profit of previous transactions should be 
done on (j-1)th day. However, the result based on that formula is also correct, because if the share was sold on j-th day and then bought again, 
it is the same if we didn't trade on that day.

So the straigtforward implementation is:

        public int MaxProfitDp(int[] prices) {
            if (prices.Length == 0) return 0;
            var dp = new int[3, prices.Length];
            for (int k = 1; k <= 2; k++)  {
                for (int i = 1; i < prices.Length; i++) {
                    int min = prices[0];
                    for (int j = 1; j <= i; j++)
                        min = Math.Min(min, prices[j] - dp[k-1, j-1]);
                    dp[k, i] = Math.Max(dp[k, i-1], prices[i] - min);
                }
            }

            return dp[2, prices.Length - 1];
        }
Time complexity is O(kn^2), space complexity is O(kn). 

Question:
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an 
integer array days. Each day is an integer from 1 to 365. Train tickets are sold in three different ways:
a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.
For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days. 
 
 
 
Solution: Dynamic Programming (Window Variant)

As in Approach 1, we only need to buy a travel pass on a day we intend to travel. Now, let dp(i) be the cost to travel from day days[i] to the end 
of the plan. If say, j1 is the largest index such that days[j1] < days[i] + 1, j7 is the largest index such that days[j7] < days[i] + 7, and j30 
is the largest index such that days[j30] < days[i] + 30, then we have:
dp(i)=min(dp(j1)+costs[0],dp(j7)+costs[1],dp(j30)+costs[2])

from functools import lru_cache

class Solution:
    def mincostTickets(self, days, costs):
        N = len(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i): # How much money to do days[i]+
            if i >= N: return 0

            ans = float('inf')
            j = i
            for c, d in zip(costs, durations):
                while j < N and days[j] < days[i] + d:
                    j += 1
                ans = min(ans, dp(j) + c)

            return ans

        return dp(0)

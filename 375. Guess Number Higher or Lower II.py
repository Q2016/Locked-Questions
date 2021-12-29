
https://leetcode.com/problems/guess-number-higher-or-lower-ii/discuss/84764/Simple-DP-solution-with-explanation~~

Explanation:
For each number x in range[i~j]
we do: result_when_pick_x = x + max{DP([i, x-1]), DP([x+1, j])}
--> // the max means whenever you choose a number, the feedback is always bad and therefore leads you to a worse branch.
then we get DP([i~j]) = min{xi, ... ,xj}
--> // this min makes sure that you are minimizing your cost.

Comment:
result_when_pick_x = x + max{DP([i~x-1]), DP([x+1, j])}

It takes me some time to understand the simple question "why it's 
using max(dp[i][x-1], dp[x+1][j])", so I want to share my understanding here to help people like me.

dp[i][j] is the minimal cost to guess from range(i...j).
When you choose an x where i <= x <= j, you may find the target number from 
left i...x-1, or you may find the target number from the x+1...j, because you 
don't know which way should go, so to guarantee you have enough money to find 
the target, you need to prepare the more, which is max(dp[i][x-1], dp[x+1][j]).



public class Solution {
    public int getMoneyAmount(int n) {
        int[][] table = new int[n+1][n+1];
        return DP(table, 1, n);
    }
    
    int DP(int[][] t, int s, int e){
        if(s >= e) return 0;
        if(t[s][e] != 0) return t[s][e];
        int res = Integer.MAX_VALUE;
        for(int x=s; x<=e; x++){
            int tmp = x + Math.max(DP(t, s, x-1), DP(t, x+1, e));
            res = Math.min(res, tmp);
        }
        t[s][e] = res;
        return res;
    }
}

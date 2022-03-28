Question:
A die simulator generates a random number from 1 to 6 for each roll. You introduced a constraint 
to the generator such that it cannot roll the number i more than rollMax[i] consecutive times.
Given an array of integers rollMax and an integer n, return the number of distinct sequences 
that can be obtained with exact n rolls. 

Example 1:
Input: n = 2, rollMax = [1,1,2,2,2,3]
Output: 34
Explanation: There will be 2 rolls of die, if there are no constraints on the die, 
there are 6 * 6 = 36 possible combinations. In this case, looking at rollMax array, 
the numbers 1 and 2 appear at most once consecutively, therefore sequences (1,1) and (2,2) 
cannot occur, so the final answer is 36-2 = 34.    






Solution: DFS

First use DFS:

    int ans = 0;
    
    public int dieSimulator(int n, int[] rollMax) {
        dfs(n, rollMax, -1, 0);
        return ans;
    }
    
	// dieLeft : the number of dies
	// last : last number we rolled
	// curlen : current len of same number
	// This function trys to traval all the valid permutation
    private void dfs(int dieLeft, int[] rollMax, int last, int curlen){
        if(dieLeft == 0){
            ans++;
            return;
        }
        for(int i=0; i<6; i++){
            if(i == last && curlen == rollMax[i]) continue;
            dfs(dieLeft - 1, rollMax, i, i == last ? curlen + 1 : 1);
        }
    }

But this will be TLE. So we add memoization:

    int[][][] dp = new int[5000][6][16];
    final int M = 1000000007;
    
    public int dieSimulator(int n, int[] rollMax) {
        return dfs(n, rollMax, -1, 0);
    }
    
    private int dfs(int dieLeft, int[] rollMax, int last, int curlen){
        if(dieLeft == 0) return 1;
        if(last >= 0 && dp[dieLeft][last][curlen] > 0) return dp[dieLeft][last][curlen];
        int ans = 0;
        for(int i=0; i<6; i++){
            if(i == last && curlen == rollMax[i]) continue;
            ans = (ans + dfs(dieLeft - 1, rollMax, i, i == last ? curlen + 1 : 1)) % M;
        }
        if(last >= 0) dp[dieLeft][last][curlen] = ans;
        return ans;
    }

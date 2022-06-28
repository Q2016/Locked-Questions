Question:
A die simulator generates a random number from 1 to 6 for each roll. You introduced a constraint 
to the generator such that it cannot roll the number i more than rollMax[i] consecutive times.
Given an array of integers rollMax and an integer n, return the number of distinct sequences 
that can be obtained with exact n rolls. 

Example 1:               1,2,3,4,5,6
Input: n = 2, rollMax = [1,1,2,2,2,3] so number 1 only 1 times, ... number 6 only 3 times etc.
Output: 34
Explanation: There will be 2 rolls of die, if there are no constraints on the die, 
there are 6 * 6 = 36 possible combinations. In this case, looking at rollMax array, 
the numbers 1 and 2 appear at most once consecutively, therefore sequences (1,1) and (2,2) 
cannot occur, so the final answer is 36-2 = 34.    





Brute force find all subsequences and check if they pass the maxroll. Or use the above example as the solution

Solution: (similar to the problem about painting houses with specific colors)

https://www.youtube.com/watch?v=zmZXG-Ds75c
	
For the house problem we had dp[i][j]=sum(dp[i-1][jj]) when j!=jj
basically to be at state with number of ways of painting ith house with color j, we need to know number of ways of painting
(i-1)th house with all color that are different from jj


For this problem: dp[i][j][k]=sum(dp[i-1][j][k-1]) for k>1 with i is the ith dice, j is like color (the number), k comes from constraint	
	          else dp[i][j][1]=sum(dp[i-1][jj][kk]) j!=jj otherwise k wont be one


Solution:
   dieSimulator(self, n, rollMax):
	dp=[[[0]*16 for _ in range(6)] for _ in range(n)]
		
	for j in raange(6):
	   dp[0][j][1]=1
	
	for i in range(1,n):
	   for j in range(6):
		for k in range(1, rollMax[j]+1):
		    if k>1:
			dp[i][j][k]=dp[i-1][j][k-1]
		    else: #k==1
			for jj in range(6):
			   for kk in range(1, rollMax[jj]+1):
				if j==jj:
				   continue
				dp[i][j][k]+=dp[i-1][jj][kk]
			
	ans=0
	for j in range(6):
	    for k in range(1, rollMax[j]+1):
		ans +=dp[n-1][j][k]
		
		
	

	
	
DFS:

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

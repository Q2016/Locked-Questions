Question:
Given an integer array nums, return the length of the longest strictly increasing subsequence. A subsequence is a 
sequence that can be derived from an array by deleting some or no elements without changing the order of the 
remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.    
    
    

    
    
    
    
    
    
Solution: DP

We need to find maximum increasing subsequence length. In the brute-force approach, we can model this problem as -

If the current element is greater than the previous element, then we can either pick it or dont pick it because we may get a smaller 
element somewhere ahead which is greater than previous and picking that would be optimal. So we try both options.
If the current element is smaller or equal to previous element, it can't be picked.
class Solution {
public:
    int lengthOfLIS(vector<int>& nums, int i = 0, int prev = INT_MIN) {
        if(i == size(nums)) return 0;
        return max(lengthOfLIS(nums, i + 1, prev), (nums[i] > prev) + lengthOfLIS(nums, i + 1, max(nums[i], prev)));
    }
};
A better and more understandable way of writing the same code as above -

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        return solve(nums, 0, INT_MIN);
    }
    int solve(vector<int>& nums, int i, int prev) {
        if(i >= size(nums)) return 0;                                // cant pick any more elements
        int take = 0, dontTake = solve(nums, i + 1, prev);           // try skipping the current element
        if(nums[i] > prev) take = 1 + solve(nums, i + 1, nums[i]);   // or pick it if it is greater than previous picked element
        return max(take, dontTake);                                  // return whichever choice gives max LIS
    }
};
Time Complexity : O(2^N), where N is the size of nums. At each index, we have choice to either take or not take the element and we explore both ways. 
So, we 2 * 2 * 2...N times = O(2^N)
Space Complexity : O(N), max recursive stack depth.

✔️ Solution - II (Dynamic Programming - Memoization)

There are many unnecessary repeated calculations in the brute-force approach. We can observe that the length of increasing subsequence starting at 
ith element with previously picked element prev will always be the same. So we can use dynamic programming to store the results for this state and 
reuse again in the future.

But it wouldn't be scalable to store the state as (i, prev) because prev element can be any number in [-104, 104] meaning we would need to 
declare a matrix dp[n][1e8] which won't be possible

DP with (i, prev) as state
Instead, we could store the state of (i, prev_i), where prev_i denotes the index of previous chosen element. Thus we would use a dp matrix where 
dp[i][j] will denote the longest increasing subsequence from index i when previous chosen element's index is j.

class Solution {
public:
    vector<vector<int>> dp;
    int lengthOfLIS(vector<int>& nums) {
        dp.resize(size(nums), vector<int>(1+size(nums), -1));   // dp[i][j] denotes max LIS starting from i when nums[j] is previous picked element
        return solve(nums, 0, -1);
    }
    int solve(vector<int>& nums, int i, int prev_i) {
        if(i >= size(nums)) return 0;
        if(dp[i][prev_i+1] != -1) return dp[i][prev_i+1];
        int take = 0, dontTake = solve(nums, i + 1, prev_i);
        // try picking current element if no previous element is chosen or current > nums[prev_i]
        if(prev_i == -1 || nums[i] > nums[prev_i]) take = 1 + solve(nums, i + 1, i); 
        return dp[i][prev_i+1] = max(take, dontTake);
    }
};
Time Complexity : O(N^2)
Space Complexity : O(N^2)

Depending on the mood of OJ, it may decide to accept your solution or give TLE for the above solution.

✔️ Solution - III (DP - Memoization - Space Optimized)

We can do better and further reduce the state stored using DP. It's redundant to store states for all i having prev as its previous element index. 
The length will always be greatest for the state (prev, prev) since no more elements before prev can be taken. So we can just use a linear DP 
where dp[i] denotes the LIS starting at index i

class Solution {
public:
    vector<int> dp;
    int lengthOfLIS(vector<int>& nums) {
        dp.resize(size(nums)+1, -1);
        return solve(nums, 0, -1);
    }
    int solve(vector<int>& nums, int i, int prev_i) {
        if(i >= size(nums)) return 0;
        if(dp[prev_i+1] != -1) return dp[prev_i+1];
        int take = 0, dontTake = solve(nums, i + 1, prev_i);
        if(prev_i == -1 || nums[i] > nums[prev_i])
            take = 1 + solve(nums, i + 1, i);
        return dp[prev_i+1] = max(take, dontTake);
    }
};
Time Complexity : O(N^2)
Space Complexity : O(N)

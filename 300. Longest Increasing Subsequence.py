Question:
Given an integer array nums, return the length of the longest strictly increasing subsequence. A subsequence is a 
sequence that can be derived from an array by deleting some or no elements without changing the order of the 
remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.    
    
    

Solution: DP

First the brute Force's idea is:
-If the current element is greater than the previous element, then we can either pick it or dont pick it 
because we may get a smaller element somewhere ahead which is greater than previous and picking that would be optimal. So we try both options.
-If the current element is smaller or equal to previous element, it can't be picked.
But it runs as O(2^N): 
    
    def lengthOfLIS(nums):
        return solve(nums, 0, INT_MIN)
    
    def solve(nums, i, prev) :
        if(i >= len(nums)) 
            return 0                                                // cant pick any more elements
        take = 0, dontTake = solve(nums, i + 1, prev)               // try skipping the current element
        if(nums[i] > prev) take = 1 + solve(nums, i + 1, nums[i])   // or pick it if it is greater than previous picked element
        return max(take, dontTake)                                  // return whichever choice gives max LIS
    
    
So we use Memoization. Let dp[i] is the longest increase subsequence which ends at nums[i].

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)


Complexity

Time: O(N^2)
Space: O(N)

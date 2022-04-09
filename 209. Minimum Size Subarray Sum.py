Question:
Given an array of positive integers nums and a positive integer target, return the minimal length of 
a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal 
to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.


Solution: sliding window 
    
Until now, we have kept the starting index of subarray fixed, and found the last position. Instead, we could move the starting 
index of the current subarray as soon as we know that no better could be done with this index as the starting index. We could keep 2 pointer,
one for the start and another for the end of the current subarray, and make optimal moves so as to keep the sum greater than ss as well 
as maintain the lowest size possible.

Algorithm

Initialize left pointer to 0 and sum to 0
Iterate over the nums:
Add nums[i] to sum
While sum is greater than or equal to s:
Update ans=min(ans,i+1−left), where i+1−left is the size of current subarray
It means that the first index can safely be incremented, since, the minimum subarray starting with this index with sum≥s has been achieved
Subtract nums[left] from sum and increment left

int minSubArrayLen(int s, vector<int>& nums)
{
    int n = nums.size();
    int ans = INT_MAX;
    int left = 0;
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += nums[i];
        while (sum >= s) {
            ans = min(ans, i + 1 - left);
            sum -= nums[left++];
        }
    }
    return (ans != INT_MAX) ? ans : 0;
}

Complexity
Time O(N)
Space O(1)

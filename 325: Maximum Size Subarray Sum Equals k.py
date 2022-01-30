Question:
Given an array nums and target value k, find the maximum length of a subarray that sums to k. If there isn’t one, return 0 instead.

Example:
Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4


Solution:
Record the sum at each index location i. If sum – k has been found before at index j, 
that means the sum of nums[j: i] is equal to k (because the sum of nums[:i] is the sum and the sum of 
nums[:j] equals sum – k). Every time we see a previous sum – k found for location i, we can check if 
the difference between the current position and the sum – k position is the longest.  
  
  
    def maxSubArrayLen(self, nums, k):

        sums = {}
        cur_sum, max_len = 0, 0
        for i in xrange(len(nums)):
            cur_sum += nums[i]
            if cur_sum == k:
                max_len = i + 1
            elif cur_sum - k in sums:
                max_len = max(max_len, i - sums[cur_sum - k])
            if cur_sum not in sums:
                sums[cur_sum] = i  # Only keep the smallest index.
        return max_len

      
# Time:  O(n)
# Space: O(n)      

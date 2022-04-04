Question:
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that 
the sum of elements in both subsets is equal.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].  
  
  
  
Solution:
  
class Solution:
    def canPartition(self, nums, i = 0, sum1 = 0, sum2 = 0):
        if i >= len(nums): return sum1 == sum2
        return self.canPartition(nums, i+1, sum1 + nums[i], sum2) or self.canPartition(nums, i+1, sum1, sum2 + nums[i])  

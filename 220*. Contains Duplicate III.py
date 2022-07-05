Question:
Given an integer array nums and two integers k and t, return true if there are two distinct 
indices i and j in the array such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true    
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
    
    
    
    
    
    
    
    
    
    
    
    
Solution:
    
The idea is like the bucket sort algorithm. Suppose we have consecutive buckets covering the range of nums with each bucket 
a width of (t+1). If there are two item with difference <= t, one of the two will happen:

(1) the two in the same bucket
(2) the two in neighbor buckets

Python

def containsNearbyAlmostDuplicate(self, nums, k, t):
    if t < 0: return False
    n = len(nums)
    d = {}
    w = t + 1
    for i in xrange(n):
        m = nums[i] / w
        if m in d:
            return True
        if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
            return True
        if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
            return True
        d[m] = nums[i]
        if i >= k: del d[nums[i - k] / w]
    return False  


O(n) time O(n) space using buckets

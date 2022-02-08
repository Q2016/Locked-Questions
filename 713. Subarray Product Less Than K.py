Question:
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements 
in the subarray is strictly less than k.

Example 1:
Input: nums = [10,5,2,6], k = 100, Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.    


Solution: Sliding window
For each right, call opt(right) the smallest left so that the product of the subarray nums[left] * nums[left + 1] * ... * nums[right] 
is less than k. opt is a monotone increasing function, so we can use a sliding window.

    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans    

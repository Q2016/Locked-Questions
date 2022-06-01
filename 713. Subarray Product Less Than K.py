Question:
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements 
in the subarray is strictly less than k.

Example 1:
Input: nums = [10,5,2,6], k = 100, Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.    










Solution: Sliding window


Link from : https://www.youtube.com/watch?v=o8OCmqYFEok
        

    def numSubarrayProductLessThanK(self, nums, k):
        left=0
        ans=0
        cur_prod=1
        
        for right, num in enumerate(nums):
            cur_prod *=num
            
            while cur_prod >=k:
                cur_prod//=nums[left]
                left +=1
                
            ans +=right-left+1
            
        return ans

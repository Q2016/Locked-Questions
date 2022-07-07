Question:
Given an array nums and target value k, find the maximum length of a subarray that sums to k. 
If there isn’t one, return 0 instead.

Example:
Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4


  
  
  
  
  
  
  
  
  
  

  
Prefix or Two pointers  
  
Solution:
  https://www.youtube.com/watch?v=ReZpa5vxRKc
  
Record the sum at each index location i. If sum – k has been found before at index j, 
that means the sum of nums[j: i] is equal to k (because the sum of nums[:i] is the sum and the sum of 
nums[:j] equals sum – k). Every time we see a previous sum – k found for location i, we can check if 
the difference between the current position and the sum – k position is the longest.  
  
  
    def maxSubArrayLen(self, nums, k):
        
        index_dict={0:-1}
        
        running_sum = 0
        ans=0 #maximum length
        
        for i, num in enumerate(nums):
            running_sum += num
            
            if running_sum - k in index_dict:
                ans = max(ans, i - index_dict[running_sum - k])
           
            if running_sum not in index_dict:
                index_dict[running_sum] = i  
        
        return ans

      
Time:  O(n)
Space: O(n)      

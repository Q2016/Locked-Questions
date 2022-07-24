Question:
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2    

    
    
    
    
    
    
    
    
    
    
Solution: cumulative sum/prefix sum
	https://www.youtube.com/watch?v=fFVZt-6sgyo
	
    
class Solution:
    def subarraySum(self, nums):
	res=0
	curSum=0		
	prefixSums={0:1}
	
	for n in nums:
	   curSum +=n
	   diff=curSum-k
	   
	   res +=prefixSums.get(diff,0)
	   prefixSums[curSum]=1+prefixSums.get(curSum,0)
	
	return res
		
		
    
    
    
Time Complexity --> O(n) // where n is the size of the array
Space Complexity --> O(n) // we are using unordered map from our side

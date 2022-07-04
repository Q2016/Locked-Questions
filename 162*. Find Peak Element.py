Question:
A peak element is an element that is strictly greater than its neighbors. Given an integer array nums, find a peak element, 
and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.    
    

Solution: Binary search
  
if an element(not the right-most one) is smaller than its right neighbor, then there must be a peak element on its right, 
because the elements on its right is either 
   1. always increasing  -> the right-most element is the peak
   2. always decreasing  -> the left-most element is the peak
   3. first increasing then decreasing -> the pivot point is the peak
   4. first decreasing then increasing -> the left-most element is the peak  
Therefore, we can find the peak only on its right elements( cut the array to half)
The same idea applies to that an element(not the left-most one) is smaller than its left neighbor.


def findPeakElement(self, nums):
    left = 0
    right = len(nums)-1

    # handle condition 3
    while left < right-1:
        mid = (left+right)/2
        if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
            return mid
            
        if nums[mid] < nums[mid+1]:
            left = mid+1
        else:
            right = mid-1
            
    #handle condition 1 and 2
    return left if nums[left] >= nums[right] else right


Run time: O(logn)
Memory: constant

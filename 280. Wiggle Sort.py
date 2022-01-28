Question:
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].


Solution:
The pattern is that numbers in odd positions are peaks. Simple method is to sort the array in increasing order and
use two pointers, one from the beginning, one from the middle. Below is the inplace solution:


    def wiggleSort(self, nums):

        for i in xrange(1, len(nums)):
            if ((i % 2) and nums[i - 1] > nums[i]) or (not (i % 2) and nums[i - 1] < nums[i]):
                # Swap unordered elements.
                nums[i - 1], nums[i] = nums[i], nums[i - 1]

                
 

# Time:  O(n)
# Space: O(1)
              

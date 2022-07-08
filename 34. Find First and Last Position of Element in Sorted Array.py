Question:
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]    



    
    
    
    
    
    
    
    
    
    
Solution:
    https://www.youtube.com/watch?v=4sQL7R5ySUU
        
class Solution:
    def searchRange(self, nums, target):
        left=self.binSearch(nums, target, True)
        right=self.binSearch(nums, target, False)
        return [left, right]
        
    # leftBias =[True/False] if false res is rightBiased    
    def binSearch(self, nums, target, leftBias):    
        l,r= 0, len(nums)-1
        i=-1
        while l<=r:
            m=(l+r)//2
            if target> nums[m]:
                l=m+1
            elif target <nums[m]:
                r=m-1
            else:
                i=m
                if leftBias:
                    r=m-1
                else:
                    l=m+1
         return i
    
    
Time complexity O(logn)

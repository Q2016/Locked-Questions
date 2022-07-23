Question:
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the 
array represents your maximum jump length at that position. Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.    


    
    
    
    
    
    
Has a tree structure and with cash can be O(n^2). But there is an O(n) with greedy.    
  
Solution:
    https://www.youtube.com/watch?v=Yan0cv2cLy8
        
class Solution:
    def canJump(self, nums):
        goal=len(nums)+1
        
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=goal:
                goal=i
        return True if goal==0 else False

Question:
Given an integer array arr and a target value target, return the integer value such that 
when we change all the integers larger than value in the given array to be equal to value, 
the sum of the array gets as close as possible (in absolute difference) to target.
In case of a tie, return the minimum such integer.
    
Example 1:
Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.

  




Solution: Binary Search (I got this comments below, I think it will help)

The value we are looking for is somewhere between 1 and maxValue (m).
Now use Binary search to speed up the process.

go up if the sum is too small
go down if the sum is too big
When we are done with binary search, l and r are equal, but it might happen that we have not exactly reached the target.
Check if l-1 (should get us below the target) leads to the sum closer to the target.

class Solution(object):
    def getRes(self,arr,t):
        nums = [t if num >= t else num for num in arr]
        return sum(nums)
    
    def findBestValue(self, arr, target):
        l = 1
        h = max(arr)
        
        while l <= h:
            mid = (h-l)//2 + l
            curr = self.getRes(arr,mid)
            if curr == target:
                return mid
            elif curr < target:
                l = mid+1
            else:
                h = mid-1
        if abs(self.getRes(arr,l) - target) < abs(self.getRes(arr,h) - target):
            return l
        return h

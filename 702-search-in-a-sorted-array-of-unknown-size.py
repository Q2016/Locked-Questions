Given an integer array sorted in ascending order, write a function to searchtargetinnums. Iftargetexists, then return its index, otherwise return-1.However, the array size is unknown to you. You may only access the array using anArrayReader interface, where ArrayReader.get(k)returns the element of the array at indexk (0-indexed).
You may assume all integers in the array are less than 10000, and if you access the array out of bounds,ArrayReader.getwill return2147483647.
Example 1:
Input:
array
 = [-1,0,3,5,9,12], 
target
 = 9

Output:
 4

Explanation:
 9 exists in 
nums
 and its index is 4
Example 2:
Input:
array
 = [-1,0,3,5,9,12], 
target
 = 2

Output:
 -1

Explanation:
 2 does not exist in 
nums
 so return -1
 
 
 
 
 
 
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        
        
        end = 1
        
        while reader.get(end) < target:            
            end *= 2
            
            
        start = 0
        
        while start + 1 < end:
            
            mid = start + (end - start) // 2
            
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) < target:
                start = mid
            else:
                end = mid
                
        
        if reader.get(start) == target:
            return start
        
        if reader.get(end) == target:
            return end
        
        return -1
Time Complexity: O(log(T)), where T is the index of the target.
Space Complexity: O(1).

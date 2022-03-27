Question:
Given an array nums of integers, a move consists of choosing any element and decreasing it by 1.

An array A is a zigzag array if either:
Every even-indexed element is greater than adjacent elements, ie. A[0] > A[1] < A[2] > A[3] < A[4] > ...
OR, every odd-indexed element is greater than adjacent elements, ie. A[0] < A[1] > A[2] < A[3] > A[4] < ...
Return the minimum number of moves to transform the given array nums into a zigzag array.


Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation: We can decrease 2 to 0 or 3 to 1.    
    

    
Solution:    


Complexity
Time O(N) for one pass
Space O(2) for two options


There are two possible ways the array can satisfy the zigzag requirement: 
1: start with a zig (increasing) 
2. start with zag (decreasing). 
There is a loop which goes through the whole list of numbers, in each step we keep track of the number of subtractions needed 
to satisfy the requiremnets for both possible ways mentioned before. We also keep track of the last modified number. 

class Solution(object):
    def movesToMakeZigzag(self, nums):
        
        zig, zag = 0, 0
        prev_zig, prev_zag = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            if i % 2 == 0:
                zig += max(0, prev_zig - nums[i] + 1)
                prev_zig = nums[i] 
                zag += max(0, nums[i] - prev_zag + 1)
                prev_zag = nums[i] - max(0, nums[i] - prev_zag + 1)
            else:
                zag += max(0, prev_zag - nums[i] + 1)
                prev_zag = nums[i]
                zig += max(0, nums[i] - prev_zig + 1)
                prev_zig = nums[i] - max(0, nums[i] - prev_zig + 1)
        
        return min(zig, zag)

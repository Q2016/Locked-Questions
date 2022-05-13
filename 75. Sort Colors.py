Question:
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

    
    
    
    
    
    
    
    
    
Solution: Dutch Partitioning

https://en.wikipedia.org/wiki/Dutch_national_flag_problem    
    
    
Pseudocode

The following pseudocode for three-way partitioning which assumes zero-based array indexing was proposed by Dijkstra himself
It uses three indices i, j and k, maintaining the invariant that i ≤ j ≤ k.

Entries from 0 up to (but not including) i are values less than mid,
entries from i up to (but not including) j are values equal to mid,
entries from j up to (and including) k are values not yet sorted, and
entries from k + 1 to the end of the array are values greater than mid.
procedure three-way-partition(A : array of values, mid : value):
    i ← 0
    j ← 0
    k ← size of A - 1

    while j <= k:
        if A[j] < mid:
            swap A[i] and A[j]
            i ← i + 1
            j ← j + 1
        else if A[j] > mid:
            swap A[j] and A[k]
            k ← k - 1
        else:
            j ← j + 1



class Solution:
    def sortColors(self, nums):
        
        p1, p2 = 0, len(nums) - 1
        p = 0
        while p <= p2:
            if nums[p] < 1:
                nums[p], nums[p1] = nums[p1], nums[p]
                p1 += 1
                p += 1
            elif nums[p] > 1:
                nums[p], nums[p2] = nums[p2], nums[p]
                p2 -= 1
            else:
                p += 1

Time: O(n) 
Space: in-place                

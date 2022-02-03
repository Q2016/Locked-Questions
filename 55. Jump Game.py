Question:
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the 
array represents your maximum jump length at that position. Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.    

Solution:
I just iterate and update the maximal index that I can reach

def canJump(A, n) :
    i = 0
    reach=0
    while i < n and i <= reach:
        reach = max(i + A[i], reach)
        i+=1
    return i == n


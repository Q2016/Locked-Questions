Question:
Given an integer array nums and two integers k and t, return true if there are two distinct 
indices i and j in the array such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true    

Solution:
    
In this problem we need to iterate over window of size k+1 and check if there is numbers with difference <=t in this window. 
What we need to do efficiently is to add and remove elements from our window, and my choice of data structure is BST, 
which is implemented in SortedList in python. So on each step we have sorted list of elements in this window. Imagine the case:
[1, 3, 7, 12] and new number we need to insert is 10, and t = 2. Then we need to consider range [8,12] and check if we have 
numbers in our SList in this range. We can do two binary searches here: bisect_left for left boundary and bisect_right 
for right boundary. Also we need to check if pos1 != len(SList), if this is the case, it means that new number is bigger 
than bigges number in list + t, so in this case we just put it directly to our list. If pos1 != pos2, this means, that we 
found some number i our [nums[i] - t, nums[i] + t] range, so we immediatly return True.



from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        SList = SortedList()
        for i in range(len(nums)):
            if i > k: SList.remove(nums[i-k-1])   
            pos1 = SortedList.bisect_left(SList, nums[i] - t)
            pos2 = SortedList.bisect_right(SList, nums[i] + t)
            
            if pos1 != pos2 and pos1 != len(SList): return True
            
            SList.add(nums[i])
        
        return False
    
Complexity: time complexity is O(n log k), because we do n steps, each one with O(log k) complexity to do binary search, 
remove and add elements. Space complexity is O(k) to keep our SortedList updated.    

Question:
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.    
    

Solution: bit manipulation
A so-called O(1) space but essencially O(N) space algorithm using bit manipulation: use each bit of number seen as the seen array in solution 1.

def findDuplicate(self, nums: List[int]) -> int:
        seen = 0
        for num in nums:
            if seen & (1 << num):
                return num
            seen |= 1 << num
            
            
            
Finding cycle

Complexity: Time complexity is O(n), because we potentially can traverse all list. Space complexity is O(1), because we actually do 
not use any extra space: our linked list is virtual.

class Solution:
    def findDuplicate(self, nums):
        slow, fast = nums[0], nums[0]
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast: break
           
        slow = nums[0];
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow

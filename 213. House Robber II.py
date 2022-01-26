Question:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of 
money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor 
of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically 
contact the police if two adjacent houses were broken into on the same night. Given an integer array nums 
representing the amount of money of each house, return the maximum amount of money you can rob tonight 
without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.    


    
Solution: DP
    
Notice that the first house and the last house can not be both robbed, so we have rob(nums) = max(rob(nums[1:], nums[:-1]). 
Since there are no circles in both nums[1:] and nums[:-1], we can simply apply the answers from House Rob. 
https://leetcode.com/problems/house-robber/discuss/299056/Python-O(n)-time-O(1)-space-4-lines

    def rob(self, nums):
                                                                                                  
        def simple_rob(nums):
            rob, not_rob = 0, 0
            for num in nums:
                rob, not_rob = not_rob + num, max(rob, not_rob)
            return max(rob, not_rob)
        
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(simple_rob(nums[1:]), simple_rob(nums[:-1]))


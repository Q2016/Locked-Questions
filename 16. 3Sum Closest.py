Question:
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).    

Solution: 3 Pointers
Similar to 3 Sum problem, use 3 pointers to point current element, next element and the last element. 
If the sum is less than target, it means we have to add a larger element so next element move to the next. 
If the sum is greater, it means we have to add a smaller element so last element move to the second 
last element. Keep doing this until the end. Each time compare the difference between sum and target, 
if it is less than minimum difference so far, then replace result with it, otherwise keep iterating.


    def threeSumClosest(self, nums, target):

        nums, result, min_diff, i = sorted(nums), float("inf"), float("inf"), 0
        while i < len(nums) - 2:
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    diff = nums[i] + nums[j] + nums[k] - target
                    if abs(diff) < min_diff:
                        min_diff = abs(diff)
                        result = nums[i] + nums[j] + nums[k]
                    if diff < 0:
                        j += 1
                    elif diff > 0:
                        k -= 1
                    else:
                        return target
            i += 1
        return result

    
    
# Time:  O(n^2)
# Space: O(1)    

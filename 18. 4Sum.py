Question:
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] 
such that:  a, b, c, and d are distinct and nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
	

	
	
	
	
	
	
	
	
	
Solution: Two Pointers
	
Similar to 3Sum. What they are really expecting at this point is a kSum solution. Therefore, 
we will focus on a generalized implementation here.
The two pointers pattern requires the array to be sorted, so we do that first. Also, it's 
easier to deal with duplicates if the array is sorted: repeated values are next to each other and easy to skip.
For 3Sum, we enumerate each value in a single loop, and use the two pointers pattern for 
the rest of the array. For kSum, we will have k - 2 nested loops to enumerate all combinations of k - 2 values.
We can implement k - 2 loops using a recursion. We will pass the starting point and k as 
the parameters. When k == 2, we will call twoSum, terminating the recursion.


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
	
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []
            # If we have run out of numbers to add, return res.
            if not nums:
                return res
            # There are k remaining values to add to the sum. The 
            # average of these values is at least target // k.
            average_value = target // k
            # We cannot obtain a sum of target if the smallest value
            # in nums is greater than target // k or if the largest 
            # value in nums is smaller than target // k.
            if average_value < nums[0] or nums[-1] < average_value:
                return res
            if k == 2:
                return twoSum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)
            return res



        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            lo, hi = 0, len(nums) - 1
    
            while (lo < hi):
                curr_sum = nums[lo] + nums[hi]
                if curr_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif curr_sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1                                     
            return res

        nums.sort()
        return kSum(nums, target, 4)

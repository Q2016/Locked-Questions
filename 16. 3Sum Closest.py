
# Time:  O(n^2)
# Space: O(1)

Similar to 3 Sum problem, use 3 pointers to point current element, next element and the last element. 
If the sum is less than target, it means we have to add a larger element so next element move to the next. 
If the sum is greater, it means we have to add a smaller element so last element move to the second 
last element. Keep doing this until the end. Each time compare the difference between sum and target, 
if it is less than minimum difference so far, then replace result with it, otherwise keep iterating.


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
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

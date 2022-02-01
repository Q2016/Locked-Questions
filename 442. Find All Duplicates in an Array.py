Question:
Given an array of integers, 1 <= a[i] <= n, some elements appear twice and others appear once. Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?

Example:
Input: [4,3,2,7,8,2,3,1], Output: [2,3]


Solution: Hash
    
O(1) space not including the input and output variables. The idea is we do a linear pass using the input array itself as a 
hash to store which numbers have been seen before. We do this by making elements at certain indexes negative. See the full explanation here    
# Time:  O(n)
# Space: O(1)
class Solution(object):
    def findDuplicates(self, nums):

        result = []
        for i in nums:
            if nums[abs(i)-1] < 0:
                result.append(abs(i))
            else:
                nums[abs(i)-1] *= -1
        return result
   

# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def findDuplicates(self, nums):

        result = []
        i = 0
        while i < len(nums):
            if nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1] 
            else:
                i += 1

        for i in xrange(len(nums)):
            if i != nums[i]-1:
                result.append(nums[i])
        return result


# Time:  O(n)
# Space: O(n), this doesn't satisfy the question
from collections import Counter
class Solution3(object):
    def findDuplicates(self, nums):

        return [elem for elem, count in Counter(nums).items() if count == 2]

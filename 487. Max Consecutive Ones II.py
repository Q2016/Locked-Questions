Question:
Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0. Follow up: What if the input 
numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large 
to hold in memory. Could you solve it efficiently?

Example 1:
Input: [1,0,1,1,0]
Output: 4


Solution:
Explanation: Flip the first zero will get the the maximum number of consecutive 1s. After flipping, the maximum number of consecutive 1s is 4.
    
    def findMaxConsecutiveOnes(self, nums):

        result, prev, curr = 0, 0, 0
        for n in nums:
            if n == 0:
                result = max(result, prev+curr+1)
                prev, curr = curr, 0
            else:
                curr += 1
        return min(max(result, prev+curr+1), len(nums))

    
    
# Time:  O(n)
# Space: O(1)    

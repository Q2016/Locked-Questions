Question:
You are playing a game involving a circular array of non-zero integers nums. Each nums[i] denotes the number of indices 
forward/backward you must move if you are located at index i:
If nums[i] is positive, move nums[i] steps forward, and
If nums[i] is negative, move nums[i] steps backward.
Since the array is circular, you may assume that moving forward from the last element puts you on the first element, 
and moving backwards from the first element puts you on the last element.
A cycle in the array consists of a sequence of indices seq of length k where: Following the movement rules above results 
in the repeating index sequence seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
Every nums[seq[j]] is either all positive or all negative. Return true if there is a cycle in nums, or false otherwise.

Example 1:
Input: nums = [2,-1,1,2,2]
Output: true
Explanation:
There is a cycle from index 0 -> 2 -> 3 -> 0 -> ...
The cycle's length is 3.


Solution: Loop in Linkedlist
Just think it as finding a loop in Linkedlist, except that loops with only 1 element do not count. Use a slow and fast pointer, 
slow pointer moves 1 step a time while fast pointer moves 2 steps a time. If there is a loop (fast == slow), we return true, 
else if we meet element with different directions, then the search fail, we set all elements along the way to 0. Because 0 is 
fail for sure so when later search meet 0 we know the search will fail.


    def circularArrayLoop(self, nums):

        def getIndex(i):
            n = len(nums)
            return (i + nums[i] + n ) % n 

        for i, val in enumerate(nums):
            if val == 0:
                continue
                
            #slow/fast pointer
            j = i
            k = getIndex(i)

            while nums[k] * nums[i] > 0 and nums[getIndex(k)] * nums[i] > 0:
                if j == k:
                    if j == getIndex(j):
                        break
                    return True

                j = getIndex(j)
                k = getIndex(getIndex(k))
                
            # loop not found, set all element along the way to 0
            j = i
            while nums[j] * val > 0:
                next = getIndex(j)
                nums[j] = 0
                j = next

        return False

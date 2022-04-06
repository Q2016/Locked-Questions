Question:
You are given an array of integers arr and an integer target. You have to find two non-overlapping sub-arrays 
of arr each with a sum equal target. There can be multiple answers so you have to find an answer where the sum
of the lengths of the two sub-arrays is minimum. Return the minimum sum of the lengths of the two required 
sub-arrays, or return -1 if you cannot find such two sub-arrays.    

Example 1:
Input: arr = [3,2,2,4,3], target = 3
Output: 2
Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2


    
Solution: Sliding window

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        INF = len(arr) + 1
        best_at_i = [INF]*len(arr) # the ith index represents the smallest length subarray we've found ending <= i that sums to target
        best = INF # output 
        curr_sum = 0 # current sum between left and right
        
        left = 0
        for right in range(len(arr)):
            # update the running sum
            curr_sum += arr[right]
            
            # arr is strictly positive, so shrink window until we're not above target
            while curr_sum > target and left <= right:
                curr_sum -= arr[left]
                left += 1
                
            if curr_sum == target:
                # we have a new shortest candidate to consider
                best = min(best, best_at_i[left-1] + right - left + 1)
                best_at_i[right] = min(best_at_i[right-1], right - left + 1)
            else:
                # best we've seen is the previous best (overlaps to end if right == 0)
                best_at_i[right] = best_at_i[right-1]
        
        if best == INF:
            return -1
        return best

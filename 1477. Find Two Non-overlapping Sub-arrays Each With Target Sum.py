Question:
You are given an array of integers arr and an integer target. You have to find two non-overlapping sub-arrays 
of arr each with a sum equal target. There can be multiple answers so you have to find an answer where the sum
of the lengths of the two sub-arrays is minimum. Return the minimum sum of the lengths of the two required 
sub-arrays, or return -1 if you cannot find such two sub-arrays.    

Example 1:
Input: arr = [3,2,2,4,3], target = 3
Output: 2
Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2


    
Solution: One-pass, prefix-sum, O(n)

Keep track of the running prefix-sum and the length of the shortest sub-array that sums to the target up to that point (best_till in my solution).
Each time we find another such sub-array, look up that length value at the index right before it starts.


    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix = {0: -1}
        best_till = [math.inf] * len(arr)
        ans = best = math.inf
        for i, curr in enumerate(itertools.accumulate(arr)):
            if curr - target in prefix:
                end = prefix[curr - target]
                if end > -1:
                    ans = min(ans, i - end + best_till[end])
                best = min(best, i - end)
            best_till[i] = best
            prefix[curr] = i
        return -1 if ans == math.inf else ans

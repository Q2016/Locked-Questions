Question:
Given an array of integers arr and an integer k. A value arr[i] is said to be stronger than a value arr[j] 
if |arr[i] - m| > |arr[j] - m| where m is the median of the array. If |arr[i] - m| == |arr[j] - m|, then arr[i] 
is said to be stronger than arr[j] if arr[i] > arr[j]. Return a list of the strongest k values in the array. 
Median is the middle value in an ordered integer list. More formally, if the length of the list is n, the median 
is the element in position ((n - 1) / 2) in the sorted list (0-indexed).
For arr = [6, -3, 7, 2, 11], n = 5 and the median is obtained by sorting the array arr = [-3, 2, 6, 7, 11] 
and the median is arr[m] where m = ((5 - 1) / 2) = 2. The median is 6.

 
Example 1:
Input: arr = [1,2,3,4,5], k = 2
Output: [5,1]
Explanation: Median is 3, the elements of the array sorted by the strongest are [5,1,4,2,3]. The strongest 2 
elements are [5, 1]. [1, 5] is also accepted answer.
Please note that although |5 - 3| == |1 - 3| but 5 is stronger than 1 because 5 > 1.    


Solution: ---

https://leetcode.com/problems/the-k-strongest-values-in-an-array/discuss/674566/Python3-straightforward-2-lines-with-custom-sort


    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        i, j = 0, len(arr) - 1
        median = arr[(len(arr) - 1) // 2] # from one of the 
        while len(arr) + i - j <= k:
            if median - arr[i] > arr[j] - median:
                i = i + 1
            else:
                j = j - 1
        return arr[:i] + arr[j + 1:]

Complexity Analysis
Time: O(n log n) for the sorting.
Memory: only what's needed for the sorting (implementation-specific), and output.

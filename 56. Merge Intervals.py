Question:
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array 
of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
    
    
    
    
    
Solution:

    
First, we sort the list as described. Then, we insert the first interval into our merged list and continue considering each 
interval in turn as follows: If the current interval begins after the previous interval ends, then they do not overlap and we 
can append the current interval to merged. Otherwise, they do overlap, and we merge them by updating the end of the previous 
interval if it is less than the end of the current interval.    
    
    
    
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key =lambda x: x[0])
        merged =[]
        for i in intervals:
			# if the list of merged intervals is empty 
			# or if the current interval does not overlap with the previous,
			# simply append it.
            if not merged or merged[-1][-1] < i[0]:
                merged.append(i)
			# otherwise, there is overlap,
			#so we merge the current and previous intervals.
            else:
                merged[-1][-1] = max(merged[-1][-1], i[-1])
        return merged
    
    
Time complexity:
In python, use sort method to a list costs O(nlogn), where n is the length of the list.
The for-loop used to merge intervals, costs O(n).
O(nlogn)+O(n) = O(nlogn)
So the total time complexity is O(nlogn).
Space complexity
The algorithm used a merged list and a variable i.
In the worst case, the merged list is equal to the length of the input intervals list. So the space complexity is O(n), 
where n is the length of the input list.
      
      
      

      


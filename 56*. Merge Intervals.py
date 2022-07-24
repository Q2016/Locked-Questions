Question:
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array 
of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
    
    
    
    
    
    
    
    
    
Solution:
https://www.youtube.com/watch?v=44H3cEC2fFM
    
class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda i:i[0])
        output=[intervals[0]]
        
        for start, end in intervals[1:]:
            lastEnd=output[-1][1]
            
            if start<=lastEnd:
                output[-1][1]=max(lastEnd, end)
            else:
                output.append([start, end])
                
        return out
             

    
    
Time complexity:
O(nlogn)+O(n) = O(nlogn)
So the total time complexity is O(nlogn).
Space complexity
The algorithm used a merged list and a variable i.
In the worst case, the merged list is equal to the length of the input intervals list. So the space complexity is O(n), 
where n is the length of the input list.
      
      
      

      


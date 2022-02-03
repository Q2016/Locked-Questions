Question:
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array 
of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
    
Solution:

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        
        start=10000
        end=0
        
        
        output=[]
        for i in intervals:
            
            if i[0]<end:# condition for intersection
                start=min(start,i[0])
                end=max(end,i[1])
            else: #if not intersect
                output.append([start,end])# send it out of the way
                start=i[0]
                end=i[1]
                
                
        return output
      
      
      

      
https://github.com/ShiqinHuo/LeetCode-Python/blob/master/Python/merge-intervals.py      
# Time:  O(nlogn)
# Space: O(1)
#
# Given a collection of intervals, merge all overlapping intervals.
# 
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].
#

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x.start)
        result = [intervals[0]]
        for i in xrange(1, len(intervals)):
            prev, current = result[-1], intervals[i]
            if current.start <= prev.end: 
                prev.end = max(prev.end, current.end)
            else:
                result.append(current)
        return result


if __name__ == "__main__":
    print Solution().merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15,18)])      

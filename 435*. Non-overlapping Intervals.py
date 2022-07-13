Question:
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you 
need to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]], Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
    
    
    
    
    
    
    
    
    
Brute-force has complexity of O(2^n). Sort by starting value, then compare and pick ones that ends first.    
    
Solution: Greedy
    
https://www.youtube.com/watch?v=nONCGxWoUfM
    
    
A classic greedy case: interval scheduling problem.

class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort()# this is interesting first by the intial then by the the secondary
        
        res=0
        prevEnd=intervals[0][1]
        for start, end in intervals[1:]:
            if start >=prevEnd:
                prevEnd=end
            else:
                res+=1
                prevEnd=min(end, prevEnd)
                
        return res

Time complexity is O(NlogN) as sort overwhelms greedy search.   

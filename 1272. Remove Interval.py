Question:
Given a sorted list of disjoint intervals, each interval intervals[i] = [a, b] represents 
the set of real numbers x such that a <= x < b.
We remove the intersections between any interval in intervals and the interval toBeRemoved.
Return a sorted list of intervals after all such removals.

Example 1:
Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6] Output: [[0,1],[6,7]] 
    
    
    
    
    
    
    
    
 Very similar to 1288. Remove Covered Intervals (solve it)   
    
    
    
    
Solution:
    
def removeInterval(self, intervals, toBeRemoved):

        removeStart, removeEnd = toBeRemoved
        output = []
        for start, end in intervals:
            if end <= removeStart or start >= removeEnd:
                output.append([start, end])
            elif start < removeStart and end > removeEnd:
                output.append([start, removeStart])
                output.append([removeEnd, end])
            elif start < removeStart and end <= removeEnd:
                output.append([start, removeStart])
            elif start >= removeStart and end > removeEnd:
                output.append([removeEnd, end])
        return output
